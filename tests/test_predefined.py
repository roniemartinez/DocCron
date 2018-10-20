#!/usr/bin/env python
# __author__ = "Ronie Martinez"
# __copyright__ = "Copyright 2018, Ronie Martinez"
# __credits__ = ["Ronie Martinez"]
# __maintainer__ = "Ronie Martinez"
# __email__ = "ronmarti18@gmail.com"
# __status__ = "Development"
from datetime import datetime, timedelta

import doccron


def test_annually():
    cron = doccron.cron('@annually')
    assert next(cron) == datetime(2019, 1, 1, 0, 0)
    assert next(cron) == datetime(2020, 1, 1, 0, 0)
    assert next(cron) == datetime(2021, 1, 1, 0, 0)


def test_yearly():
    cron = doccron.cron('@yearly')
    assert next(cron) == datetime(2019, 1, 1, 0, 0)
    assert next(cron) == datetime(2020, 1, 1, 0, 0)
    assert next(cron) == datetime(2021, 1, 1, 0, 0)


def test_monthly():
    cron = doccron.cron('@monthly')
    next_month = datetime.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    for _ in range(3):
        if next_month.month == 12:
            next_month = next_month.replace(year=next_month.year+1, month=1)
        else:
            next_month = next_month.replace(month=next_month.month+1)
        assert next(cron) == next_month


def test_weekly():
    cron = doccron.cron('@weekly')
    next_sunday = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    while next_sunday.isoweekday() != 7:
        next_sunday += timedelta(days=1)
    assert next(cron) == next_sunday
    for _ in range(3):
        next_sunday += timedelta(days=7)
        assert next(cron) == next_sunday


def test_daily():
    cron = doccron.cron('@daily')
    next_day = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    for _ in range(3):
        next_day += timedelta(days=1)
        assert next(cron) == next_day


def test_hourly():
    cron = doccron.cron('@hourly')
    next_hour = datetime.now().replace(minute=0, second=0, microsecond=0)
    for _ in range(3):
        next_hour += timedelta(hours=1)
        assert next(cron) == next_hour


def test_reboot():
    cron = doccron.cron('@reboot')
    # since granularity is per minute, @reboot is equivalent to the next minute
    next_minute = datetime.now().replace(second=0, microsecond=0) + timedelta(minutes=1)
    assert next(cron) == next_minute
    assert next(cron) is None
