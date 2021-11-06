from collections.abc import Iterator
from datetime import datetime, timedelta

import pytest
from dateutil.tz import tzlocal

import doccron
from doccron import InvalidSchedule
from doccron.interval_job import IntervalJob


def test_every_2_hours() -> None:
    cron = doccron.cron("@every 2h")
    next_schedule = datetime.now(tz=tzlocal()).replace(microsecond=0)
    for _ in range(12):
        next_schedule += timedelta(hours=2)
        assert next(cron) == next_schedule


def test_every_2_minutes() -> None:
    cron = doccron.cron("@every 2m")
    next_schedule = datetime.now(tz=tzlocal()).replace(microsecond=0)

    for _ in range(60):
        next_schedule += timedelta(minutes=2)
        assert next(cron) == next_schedule


def test_every_2_hours_30_minutes() -> None:
    cron = doccron.cron("@every 2h30m")
    next_schedule = datetime.now(tz=tzlocal()).replace(microsecond=0)

    for _ in range(3):
        next_schedule += timedelta(hours=2, minutes=30)
        assert next(cron) == next_schedule


def test_every_2_hours_30_minutes_4_seconds() -> None:
    cron = doccron.cron("@every 2h30m5s")
    next_schedule = datetime.now(tz=tzlocal()).replace(microsecond=0)

    for _ in range(3):
        next_schedule += timedelta(hours=2, minutes=30, seconds=5)
        assert next(cron) == next_schedule


def test_invalid_string() -> None:
    with pytest.raises(InvalidSchedule):
        doccron.cron("@every hello")


def test_iter_interval_job() -> None:
    job = iter(IntervalJob(timedelta(minutes=2)))
    assert isinstance(job, Iterator)
