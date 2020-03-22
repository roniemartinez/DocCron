#!/usr/bin/env python
# __author__ = "Ronie Martinez"
# __copyright__ = "Copyright 2018-2020, Ronie Martinez"
# __credits__ = ["Ronie Martinez"]
# __maintainer__ = "Ronie Martinez"
# __email__ = "ronmarti18@gmail.com"
from datetime import timedelta

from dateutil.tz import tzfile, tzlocal, tzwin  # type: ignore

from doccron.cron_job import CronJob
from doccron.exceptions import InvalidSchedule
from doccron.interval_job import IntervalJob


class CronTable(object):
    def __init__(self, jobs, quartz=False):
        self._jobs = {}
        self._previous_schedule = None
        self._timezone = tzlocal()
        for j in jobs:
            if isinstance(j, tzfile):
                self._timezone = j
                continue
            try:
                if isinstance(j, tzwin):
                    self._timezone = j
                    continue
            except TypeError:
                pass
            if isinstance(j, timedelta):
                job = IntervalJob(j, quartz, timezone=self._timezone)
            else:
                try:
                    job = CronJob(j, quartz=quartz, timezone=self._timezone)
                except ValueError:
                    raise InvalidSchedule
            self._jobs[job] = next(job)

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if not len(self._jobs):
                return
            job, next_schedule = sorted(self._jobs.items(), key=lambda x: x[1])[0]
            if next_schedule is None:
                del self._jobs[job]
                return
            self._jobs[job] = next(job)
            if self._previous_schedule and next_schedule <= self._previous_schedule:
                continue
            self._previous_schedule = next_schedule
            return next_schedule
