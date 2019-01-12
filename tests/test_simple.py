#!/usr/bin/env python
# __author__ = "Ronie Martinez"
# __copyright__ = "Copyright 2018-2019, Ronie Martinez"
# __credits__ = ["Ronie Martinez"]
# __maintainer__ = "Ronie Martinez"
# __email__ = "ronmarti18@gmail.com"
try:
    from collections.abc import Iterator
except ImportError:
    from collections import Iterator
from datetime import datetime, timedelta

# noinspection PyPackageRequirements
import pytest

import doccron
from doccron.job import Job
from doccron.table import InvalidSchedule


def test_comments():
    cron = doccron.cron('# * * * * *')
    assert next(cron) is None


def test_invalid_strings():
    with pytest.raises(InvalidSchedule):
        doccron.cron('hello')


def test_iter_cron_table():
    cron = iter(doccron.cron('* * * * *'))
    assert isinstance(cron, Iterator)


def test_iter_job():
    job = iter(Job(['*'] * 5))
    assert isinstance(job, Iterator)


def test_not_repeated():
    cron = doccron.cron('* * * * *\n* * * * *')
    first = next(cron)
    second = next(cron)
    assert first < second


def test_schedule_per_minute():
    current_datetime = datetime.now().replace(second=0, microsecond=0)
    cron = doccron.cron('* * * * *')
    assert isinstance(cron, Iterator)

    for i in range(1, 6):
        # noinspection PyTypeChecker
        next_schedule = next(cron)
        assert isinstance(next_schedule, datetime)
        assert next_schedule == current_datetime + timedelta(minutes=i)


def test_before_year_end():
    cron = doccron.cron('59 23 31 12 5 *')
    assert next(cron) == datetime(2021, 12, 31, 23, 59)
    assert next(cron) == datetime(2027, 12, 31, 23, 59)
    assert next(cron) == datetime(2032, 12, 31, 23, 59)


def test_abbreviated_month_name():
    cron = doccron.cron('59 23 31 dec 5 *')
    assert next(cron) == datetime(2021, 12, 31, 23, 59)
    assert next(cron) == datetime(2027, 12, 31, 23, 59)
    assert next(cron) == datetime(2032, 12, 31, 23, 59)


def test_abbreviated_weekday_name():
    cron = doccron.cron('59 23 31 12 fri *')
    assert next(cron) == datetime(2021, 12, 31, 23, 59)
    assert next(cron) == datetime(2027, 12, 31, 23, 59)
    assert next(cron) == datetime(2032, 12, 31, 23, 59)


def test_passed():
    cron = doccron.cron('45 17 7 6 * 2001,2002')
    assert next(cron) is None
