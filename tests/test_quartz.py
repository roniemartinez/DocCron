#!/usr/bin/env python
# __author__ = "Ronie Martinez"
# __copyright__ = "Copyright 2018, Ronie Martinez"
# __credits__ = ["Ronie Martinez"]
# __maintainer__ = "Ronie Martinez"
# __email__ = "ronmarti18@gmail.com"
# __status__ = "Production"
from collections import Iterable
from datetime import datetime, timedelta

import doccron
from doccron.job import Job


def test_iter_cron_table():
    cron = iter(doccron.cron_quartz('* * * * * *'))
    assert isinstance(cron, Iterable)


def test_iter_job():
    job = iter(Job(['*'] * 6, quartz=True))
    assert isinstance(job, Iterable)


def test_not_repeated():
    cron = doccron.cron_quartz('* * * * * *\n* * * * * *')
    first = next(cron)
    second = next(cron)
    assert first < second


def test_schedule_per_second():
    cron = doccron.cron_quartz('* * * * * *')
    assert isinstance(cron, Iterable)

    next_schedule = next(cron)
    assert next_schedule > datetime.now().replace(microsecond=0)
    assert isinstance(next_schedule, datetime)
    for i in range(10):
        n = next(cron)
        assert isinstance(n, datetime)
        assert next_schedule + timedelta(seconds=1) == n
        next_schedule = n


def foo():
    """
    * * * * * * 2021
    * * * * * * 2020
    """
    print("foo")


def test_find_functions_with_docstrings():
    run_count = 0
    for next_schedule, function_object in doccron.run_jobs(quartz=True, simulate=True):
        assert isinstance(next_schedule, datetime)
        assert function_object.__name__ == 'foo'
        run_count += 1
        if run_count == 5:
            break
