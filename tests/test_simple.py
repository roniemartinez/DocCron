from collections.abc import Iterator
from datetime import datetime, timedelta

import pytest
from dateutil.tz import tzlocal
from freezegun import freeze_time

import doccron
from doccron.cron_job import CronJob
from doccron.exceptions import InvalidSchedule
from doccron.timezone import localize


def test_comments() -> None:
    cron = doccron.cron("# * * * * *")
    assert next(cron) is None


def test_invalid_strings() -> None:
    with pytest.raises(InvalidSchedule):
        doccron.cron("hello")


def test_iter_cron_table() -> None:
    cron = iter(doccron.cron("* * * * *"))
    assert isinstance(cron, Iterator)


def test_iter_cron_job() -> None:
    job = iter(CronJob(["*"] * 5))
    assert isinstance(job, Iterator)


def test_not_repeated() -> None:
    cron = doccron.cron("* * * * *\n* * * * *")
    first = next(cron)
    second = next(cron)
    assert first < second


def test_schedule_per_minute() -> None:
    current_datetime = datetime.now(tz=tzlocal()).replace(second=0, microsecond=0)
    cron = doccron.cron("* * * * *")
    assert isinstance(cron, Iterator)

    for i in range(1, 6):
        next_schedule = next(cron)
        assert isinstance(next_schedule, datetime)
        assert next_schedule == current_datetime + timedelta(minutes=i)


@freeze_time("2020-01-01")
def test_before_year_end() -> None:
    cron = doccron.cron("59 23 31 12 5 *")
    assert next(cron) == localize(datetime(2021, 12, 31, 23, 59))
    assert next(cron) == localize(datetime(2027, 12, 31, 23, 59))
    assert next(cron) == localize(datetime(2032, 12, 31, 23, 59))


@freeze_time("2020-01-01")
def test_abbreviated_month_name() -> None:
    cron = doccron.cron("59 23 31 dec 5 *")
    assert next(cron) == localize(datetime(2021, 12, 31, 23, 59))
    assert next(cron) == localize(datetime(2027, 12, 31, 23, 59))
    assert next(cron) == localize(datetime(2032, 12, 31, 23, 59))


@freeze_time("2020-01-01")
def test_abbreviated_weekday_name() -> None:
    cron = doccron.cron("59 23 31 12 fri *")
    assert next(cron) == localize(datetime(2021, 12, 31, 23, 59))
    assert next(cron) == localize(datetime(2027, 12, 31, 23, 59))
    assert next(cron) == localize(datetime(2032, 12, 31, 23, 59))


def test_passed() -> None:
    cron = doccron.cron("45 17 7 6 * 2001,2002")
    assert next(cron) is None
