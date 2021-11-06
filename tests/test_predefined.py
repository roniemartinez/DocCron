from datetime import datetime, timedelta

from dateutil.tz import tzlocal

import doccron
from doccron.timezone import localize


def test_annually() -> None:
    cron = doccron.cron("@annually")
    now = datetime.now(tz=tzlocal())
    year = now.year if now < localize(datetime(now.year, 1, 1)) else now.year + 1
    assert next(cron) == localize(datetime(year, 1, 1, 0, 0))
    assert next(cron) == localize(datetime(year + 1, 1, 1, 0, 0))
    assert next(cron) == localize(datetime(year + 2, 1, 1, 0, 0))


def test_yearly() -> None:
    cron = doccron.cron("@yearly")
    now = datetime.now(tz=tzlocal())
    year = now.year if now < localize(datetime(now.year, 1, 1)) else now.year + 1
    assert next(cron) == localize(datetime(year, 1, 1, 0, 0))
    assert next(cron) == localize(datetime(year + 1, 1, 1, 0, 0))
    assert next(cron) == localize(datetime(year + 2, 1, 1, 0, 0))


def test_monthly() -> None:
    cron = doccron.cron("@monthly")
    next_month = datetime.now(tz=tzlocal()).replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    for _ in range(3):
        if next_month.month == 12:
            next_month = next_month.replace(year=next_month.year + 1, month=1)
        else:
            next_month = next_month.replace(month=next_month.month + 1)
        assert next(cron) == next_month


def test_weekly() -> None:
    cron = doccron.cron("@weekly")
    next_sunday = datetime.now(tz=tzlocal()).replace(hour=0, minute=0, second=0, microsecond=0)
    while next_sunday.isoweekday() != 7:
        next_sunday += timedelta(days=1)
    if next_sunday <= datetime.now(tz=tzlocal()):
        next_sunday += timedelta(days=7)
    assert next(cron) == next_sunday
    for _ in range(3):
        next_sunday += timedelta(days=7)
        assert next(cron) == next_sunday


def test_daily() -> None:
    cron = doccron.cron("@daily")
    next_day = datetime.now(tz=tzlocal()).replace(hour=0, minute=0, second=0, microsecond=0)
    for _ in range(3):
        next_day += timedelta(days=1)
        assert next(cron) == next_day


def test_midnight() -> None:
    cron = doccron.cron("@midnight")
    next_day = datetime.now(tz=tzlocal()).replace(hour=0, minute=0, second=0, microsecond=0)
    for _ in range(3):
        next_day += timedelta(days=1)
        assert next(cron) == next_day


def test_hourly() -> None:
    cron = doccron.cron("@hourly")
    next_hour = datetime.now(tz=tzlocal()).replace(minute=0, second=0, microsecond=0)
    for _ in range(3):
        next_hour += timedelta(hours=1)
        assert next(cron) == next_hour


def test_reboot() -> None:
    cron = doccron.cron("@reboot")
    # since granularity is per minute, @reboot is equivalent to the next minute
    next_minute = datetime.now(tz=tzlocal()).replace(second=0, microsecond=0) + timedelta(minutes=1)
    assert next(cron) == next_minute
    assert next(cron) is None
