#!/usr/bin/env python
# __author__ = "Ronie Martinez"
# __copyright__ = "Copyright 2018-2020, Ronie Martinez"
# __credits__ = ["Ronie Martinez"]
# __maintainer__ = "Ronie Martinez"
# __email__ = "ronmarti18@gmail.com"
from datetime import datetime, timedelta

from dateutil.tz import tzlocal

import doccron


def test_minute_range():
    cron = doccron.cron("5-20 * * * * *")
    next_datetime = datetime.now(tz=tzlocal()).replace(second=0, microsecond=0)

    for _ in range(25):
        while True:
            if next_datetime.minute in range(5, 21) and next_datetime > datetime.now(
                tz=tzlocal()
            ):
                break
            next_datetime += timedelta(minutes=1)
        next_schedule = next(cron)  # type: datetime
        assert isinstance(next_schedule, datetime)
        assert next_schedule == next_datetime
        next_datetime += timedelta(minutes=1)


def test_hour_range():
    cron = doccron.cron("* 5-20 * * * *")
    next_datetime = datetime.now(tz=tzlocal()).replace(second=0, microsecond=0)
    next_datetime += timedelta(minutes=1)

    for _ in range(25):
        while True:
            if next_datetime.hour in range(5, 21) and next_datetime > datetime.now(
                tz=tzlocal()
            ):
                break
            next_datetime += timedelta(minutes=1)
        next_schedule = next(cron)  # type: datetime
        assert isinstance(next_schedule, datetime)
        assert next_schedule == next_datetime
        next_datetime += timedelta(minutes=1)


def test_day_range():
    cron = doccron.cron("* * 20-25 * * *")
    next_datetime = datetime.now(tz=tzlocal()).replace(
        hour=0, minute=0, second=0, microsecond=0
    )

    for _ in range(25):
        while next_datetime.day not in range(20, 26):
            next_datetime += timedelta(days=1)
        while next_datetime <= datetime.now(tz=tzlocal()):
            next_datetime += timedelta(minutes=1)
        next_schedule = next(cron)  # type: datetime
        assert isinstance(next_schedule, datetime)
        assert next_schedule == next_datetime
        next_datetime += timedelta(minutes=1)


def test_weekday_number_range():
    cron = doccron.cron("0 10 * * 1-5 *")
    next_datetime = datetime.now(tz=tzlocal()).replace(
        hour=10, minute=0, second=0, microsecond=0
    )
    while True:
        if next_datetime.isoweekday() in range(1, 6) and next_datetime > datetime.now(
            tz=tzlocal()
        ):
            break
        next_datetime += timedelta(days=1)
    next_schedule = next(cron)  # type: datetime
    assert isinstance(next_schedule, datetime)
    assert next_schedule == next_datetime


def test_weekday_name_range():
    cron = doccron.cron("0 10 * * TUE-FRI *")
    next_datetime = datetime.now(tz=tzlocal()).replace(
        hour=10, minute=0, second=0, microsecond=0
    )
    while True:
        if next_datetime.isoweekday() in range(2, 6) and next_datetime > datetime.now(
            tz=tzlocal()
        ):
            break
        next_datetime += timedelta(days=1)
    next_schedule = next(cron)  # type: datetime
    assert isinstance(next_schedule, datetime)
    assert next_schedule == next_datetime


def test_month_number_range():
    cron = doccron.cron("0 10 1 2-8 * *")
    next_datetime = datetime.now(tz=tzlocal()).replace(
        day=1, hour=10, minute=0, second=0, microsecond=0
    )
    while True:
        if (
            next_datetime.month in range(2, 9)
            and next_datetime.day == 1
            and next_datetime > datetime.now(tz=tzlocal())
        ):
            break
        next_datetime += timedelta(days=1)
    next_schedule = next(cron)  # type: datetime
    assert isinstance(next_schedule, datetime)
    assert next_schedule == next_datetime


def test_month_name_range():
    cron = doccron.cron("0 10 1 Mar-Nov * *")
    next_datetime = datetime.now(tz=tzlocal()).replace(
        day=1, hour=10, minute=0, second=0, microsecond=0
    )
    while True:
        if (
            next_datetime.month in range(3, 12)
            and next_datetime.day == 1
            and next_datetime > datetime.now(tz=tzlocal())
        ):
            break
        next_datetime += timedelta(days=1)
    next_schedule = next(cron)  # type: datetime
    assert isinstance(next_schedule, datetime)
    assert next_schedule == next_datetime


def test_year_range():
    cron = doccron.cron("0 10 1 2 * 2020-2030")
    next_datetime = datetime.now(tz=tzlocal()).replace(
        month=2, day=1, hour=10, minute=0, second=0, microsecond=0
    )
    while True:
        if (
            next_datetime.year in range(2020, 2031)
            and next_datetime.month == 2
            and next_datetime.day == 1
            and next_datetime > datetime.now(tz=tzlocal())
        ):
            break
        next_datetime = next_datetime.replace(year=next_datetime.year + 1)
    next_schedule = next(cron)  # type: datetime
    assert isinstance(next_schedule, datetime)
    assert next_schedule == next_datetime
