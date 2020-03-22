#!/usr/bin/env python
# __author__ = "Ronie Martinez"
# __copyright__ = "Copyright 2018-2020, Ronie Martinez"
# __credits__ = ["Ronie Martinez"]
# __maintainer__ = "Ronie Martinez"
# __email__ = "ronmarti18@gmail.com"
import inspect
import logging
import re
import threading
import time
from datetime import datetime, timedelta, tzinfo
from typing import Iterator, Optional, Union

from dateutil.tz import tz, tzlocal

from doccron.exceptions import InvalidSchedule
from doccron.table import CronTable

logger = logging.getLogger("doccron")

DURATION = re.compile(r"((?P<hours>\d+)h)?((?P<minutes>\d+)m)?((?P<seconds>\d+)s)?")


def parse_duration(duration: str) -> timedelta:
    match = DURATION.match(duration)
    if not match:
        raise InvalidSchedule
    matches = match.groupdict(default="0")
    return timedelta(
        hours=int(matches["hours"]),
        minutes=int(matches["minutes"]),
        seconds=int(matches["seconds"]),
    )


def _tokenize_by_percent(jobs: str) -> Iterator[Union[timedelta, list]]:
    for job in jobs.split("%"):
        job = job.strip()
        if job.startswith("@every"):
            interval = job.split(" ", 2)[1]
            yield parse_duration(interval)
            continue
        elif job.startswith("@"):
            job = {
                "@annually": "0 0 1 1 *",
                "@yearly": "0 0 1 1 *",
                "@monthly": "0 0 1 * *",
                "@weekly": "0 0 * * 0",
                "@daily": "0 0 * * *",
                "@midnight": "0 0 * * *",
                "@hourly": "0 * * * *",
                "@reboot": _next_minute(),
            }[job]
        elif job.startswith("#"):
            continue
        elif "?" in job:
            job = job.replace("?", "*")
        yield job.split(None, 6)


def tokenize(
    jobs: Union[list, str], quartz=False
) -> Iterator[Union[timedelta, Optional[tzinfo], list]]:
    if isinstance(jobs, str):
        job_list = jobs.splitlines()
    else:
        job_list = jobs
    for job in job_list:  # type: str
        job = job.strip()
        if job.startswith("CRON_TZ"):
            yield tz.gettz(job.split("=", 2)[1].strip())
            continue
        for tokens in _tokenize_by_percent(job):
            if isinstance(tokens, timedelta):
                yield tokens
                continue
            length = len(tokens)
            if quartz:
                tokens += ["*"] * (7 - length)
            else:
                tokens += ["*"] * (6 - length)
            yield tokens


def parse_schedules(docstring):
    lines = iter(docstring.splitlines())
    schedules = {"cron": []}
    for line in lines:
        if line.strip() == "/etc/crontab::":
            leading_whitespaces = len(line) - len(line.lstrip())
            assert len(next(lines).strip()) == 0
            indented = None
            while True:
                try:
                    line = next(lines)
                    schedule = line.strip()
                    if indented is None:
                        indented = len(line) - len(line.lstrip()) > leading_whitespaces
                    if (
                        indented
                        and len(line) - len(line.lstrip()) <= leading_whitespaces
                    ):
                        break
                    if len(schedule) and schedule[0] not in ":@":
                        schedules["cron"].append(schedule)
                    else:
                        break
                except StopIteration:
                    break
    return schedules


def _next_minute():
    next_minute = datetime.now(tz=tzlocal()).replace(
        second=0, microsecond=0
    ) + timedelta(minutes=1)
    return "{} {} {} {} * {}".format(
        next_minute.minute,
        next_minute.hour,
        next_minute.day,
        next_minute.month,
        next_minute.year,
    )


def cron(jobs: Union[str, list], quartz: bool = False) -> CronTable:
    return CronTable(tokenize(jobs), quartz=quartz)


def cron_quartz(jobs: Union[str, list]) -> CronTable:
    return cron(jobs, quartz=True)


def _job_iter(job_function_map):
    job_map = {}
    for job in job_function_map.keys():
        job_map[job] = next(job)
    while True:
        job, next_schedule = sorted(job_map.items(), key=lambda x: x[1])[0]
        if next_schedule:
            yield next_schedule, job_function_map[job]
        else:
            break
        job_map[job] = next(job)


def run_jobs(quartz: bool = False, simulate: bool = False):
    job_function_map = {}
    logger.info("Searching jobs")
    for function_object in inspect.currentframe().f_back.f_globals.values():  # type: ignore
        if inspect.isfunction(function_object):
            docstring = inspect.getdoc(function_object)
            if docstring and isinstance(docstring, str):
                docstring = docstring.strip()
                if len(docstring):
                    schedules = parse_schedules(docstring)
                    cron_schedules = schedules["cron"]
                    if len(cron_schedules):
                        job_function_map[
                            cron(cron_schedules, quartz=quartz)
                        ] = function_object
    if simulate:
        logger.info("Simulation started")
        return _job_iter(job_function_map)
    _run_jobs(job_function_map)  # pragma: no cover


def _run_jobs(job_function_map):  # pragma: no cover
    """
    Executes all scheduled functions. Not testable at the moment due to threading. Excluded from code coverage.
    :param job_function_map:
    """
    threads = []
    for next_schedule, function_object in _job_iter(job_function_map):
        thread_count = len(threads)
        if thread_count == len(job_function_map):
            while True:
                thread = threads[thread_count - 1]  # type: threading.Thread
                if not thread.is_alive():
                    interval = next_schedule - datetime.now(
                        tz=tzlocal()
                    )  # type: timedelta
                    thread = threading.Timer(
                        interval.total_seconds(), function_object
                    )  # type: threading.Thread
                    threads[thread_count - 1] = thread
                    logger.info(
                        "Scheduling function '%s' to run at %s",
                        function_object.__name__,
                        next_schedule.strftime("%Y-%m-%d %H:%M:%S%z"),
                    )
                    thread.start()
                    break
                thread_count = (
                    len(job_function_map) if thread_count == 1 else thread_count - 1
                )
                time.sleep(1)
        else:
            interval = next_schedule - datetime.now(tz=tzlocal())  # type: timedelta
            thread = threading.Timer(
                interval.total_seconds(), function_object
            )  # type: threading.Thread
            threads.append(thread)
            thread.start()
            logger.info(
                "Scheduling function '%s' to run at %s",
                function_object.__name__,
                next_schedule.strftime("%Y-%m-%d %H:%M:%S%z"),
            )
    if len(threads):
        for thread in threads:
            thread.join()
        logger.info("Finished executing jobs")
    else:
        logger.info("No jobs found")
