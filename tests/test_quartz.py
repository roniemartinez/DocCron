from collections.abc import Iterator
from datetime import datetime, timedelta

from dateutil.tz import tzlocal
from freezegun import freeze_time

import doccron
from doccron.cron_job import CronJob


def test_iter_cron_table() -> None:
    cron = iter(doccron.cron_quartz("* * * * * *"))
    assert isinstance(cron, Iterator)


def test_iter_job() -> None:
    job = iter(CronJob(["*"] * 6, quartz=True))
    assert isinstance(job, Iterator)


def test_not_repeated() -> None:
    cron = doccron.cron_quartz("* * * * * *\n* * * * * *")
    first = next(cron)
    second = next(cron)
    assert first < second


def test_schedule_per_second() -> None:
    cron = doccron.cron_quartz("* * * * * *")
    assert isinstance(cron, Iterator)

    next_schedule = next(cron)
    assert next_schedule > datetime.now(tz=tzlocal()).replace(microsecond=0)
    assert isinstance(next_schedule, datetime)
    for i in range(10):
        n = next(cron)
        assert isinstance(n, datetime)
        assert next_schedule + timedelta(seconds=1) == n
        next_schedule = n


def test_schedule_per_second_list() -> None:
    cron = doccron.cron_quartz("0,10,20,30,40,50 * * * * * *")
    assert isinstance(cron, Iterator)

    next_schedule = next(cron)
    assert next_schedule > datetime.now(tz=tzlocal()).replace(microsecond=0)
    assert isinstance(next_schedule, datetime)
    for i in range(0, 60, 10):
        n = next(cron)
        assert isinstance(n, datetime)
        assert next_schedule + timedelta(seconds=10) == n
        next_schedule = n


def test_schedule_per_second_range_step() -> None:
    cron = doccron.cron_quartz("0-59/10 * * * * * *")
    assert isinstance(cron, Iterator)

    next_schedule = next(cron)
    assert next_schedule > datetime.now(tz=tzlocal()).replace(microsecond=0)
    assert isinstance(next_schedule, datetime)
    for i in range(0, 60, 10):
        n = next(cron)
        assert isinstance(n, datetime)
        assert next_schedule + timedelta(seconds=10) == n
        next_schedule = n


def foo() -> None:
    """
    /etc/crontab::

        * * * * * * 2021
        * * * * * * 2020
    """
    print("foo")


@freeze_time("2020-01-01")
def test_find_functions_with_docstrings() -> None:
    run_count = 0
    jobs_found = False
    for next_schedule, function_object in doccron.run_jobs(quartz=True, simulate=True):
        assert isinstance(next_schedule, datetime)
        assert function_object.__name__ == "foo"
        jobs_found = True
        run_count += 1
        if run_count == 5:
            break
    assert jobs_found
