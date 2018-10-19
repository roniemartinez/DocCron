#!/usr/bin/env python
# __author__ = "Ronie Martinez"
# __copyright__ = "Copyright 2018, Ronie Martinez"
# __credits__ = ["Ronie Martinez"]
# __maintainer__ = "Ronie Martinez"
# __email__ = "ronmarti18@gmail.com"
# __status__ = "Development"
from datetime import datetime, timedelta
from typing import Iterable

import doccron


def test_schedule_per_minute():
    current_datetime = datetime.now().replace(second=0, microsecond=0)
    cron = doccron.cron('* * * * *')
    assert isinstance(cron, doccron.CronTable)
    assert isinstance(cron, Iterable)

    for i in range(1, 6):
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
