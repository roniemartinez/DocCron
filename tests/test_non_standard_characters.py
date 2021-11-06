from calendar import monthrange
from datetime import datetime, timedelta

from dateutil.tz import tzlocal

import doccron
from doccron.timezone import localize


def test_question_mark() -> None:
    current_year = datetime.now(tz=tzlocal()).year
    cron = doccron.cron("45 17 7 6 ? {},{}".format(current_year + 1, current_year + 2))
    assert next(cron) == localize(datetime(current_year + 1, 6, 7, 17, 45))
    assert next(cron) == localize(datetime(current_year + 2, 6, 7, 17, 45))


def test_last_day_of_month() -> None:
    now = datetime.now(tz=tzlocal())
    first_year = now.year if now < localize(datetime(now.year, 6, 30)) else now.year + 1
    cron = doccron.cron("* * L 6 ? *")

    assert next(cron) == localize(datetime(first_year, 6, 30, 0, 0))
    assert next(cron) == localize(datetime(first_year, 6, 30, 0, 1))


def test_last_day_of_week_of_month() -> None:
    cron = doccron.cron("0 0 * * 5L *")
    last_friday = datetime.now(tz=tzlocal()).replace(hour=0, minute=0, second=0, microsecond=0)
    while last_friday.isoweekday() != 5:
        last_friday += timedelta(days=1)
    for _ in range(3):
        while last_friday.month == (last_friday + timedelta(days=7)).month:
            last_friday += timedelta(days=7)
        assert next(cron) == last_friday
        last_friday += timedelta(days=7)


def test_exact_weekday_of_month_should_not_move() -> None:
    cron = doccron.cron("0 0 21W * 1 2050")
    datetime_21 = localize(datetime(2050, 1, 21)).replace(hour=0, minute=0, second=0, microsecond=0)
    if datetime_21.day == 21:
        datetime_21 += timedelta(days=monthrange(datetime_21.year, datetime_21.month)[-1])
    while True:
        if datetime_21.day == 21 and datetime_21.isoweekday() in range(1, 6):
            break
        datetime_21 += timedelta(days=1)
    assert next(cron) == datetime_21


def test_saturday_should_go_back_to_friday() -> None:
    cron = doccron.cron("0 0 21W * 6 *")
    datetime_21 = datetime.now(tz=tzlocal()).replace(hour=0, minute=0, second=0, microsecond=0)
    if datetime_21.day == 21:
        datetime_21 += timedelta(days=monthrange(datetime_21.year, datetime_21.month)[-1])
    while True:
        if datetime_21.day == 21 and datetime_21.isoweekday() == 6:
            break
        datetime_21 += timedelta(days=1)
    assert next(cron) == datetime_21 - timedelta(days=1)


def test_first_day_of_month_saturday_should_move_to_monday() -> None:
    cron = doccron.cron("0 0 1W * 6 *")
    datetime_1 = datetime.now(tz=tzlocal()).replace(hour=0, minute=0, second=0, microsecond=0)
    if datetime_1.day == 1:
        datetime_1 += timedelta(days=monthrange(datetime_1.year, datetime_1.month)[-1])
    while True:
        if datetime_1.day == 1 and datetime_1.isoweekday() == 6:
            break
        datetime_1 += timedelta(days=1)
    assert next(cron) == datetime_1 + timedelta(days=2)


def test_sunday_should_move_to_monday() -> None:
    cron = doccron.cron("0 0 21W * 7 *")
    datetime_21 = datetime.now(tz=tzlocal()).replace(hour=0, minute=0, second=0, microsecond=0)
    if datetime_21.day == 21:
        datetime_21 += timedelta(days=monthrange(datetime_21.year, datetime_21.month)[-1])
    while True:
        if datetime_21.day == 21 and datetime_21.isoweekday() == 7:
            break
        datetime_21 += timedelta(days=1)
    assert next(cron) == datetime_21 + timedelta(days=1)


def test_hash() -> None:
    cron = doccron.cron("0 0 * * 7#2 *")
    second_sunday = datetime.now(tz=tzlocal()).replace(hour=0, minute=0, second=0, microsecond=0)
    while True:
        second_sunday += timedelta(days=1)
        if second_sunday.isoweekday() == 7:
            break
    while True:
        if (
            second_sunday.month == (second_sunday - timedelta(days=7)).month
            and second_sunday.month != (second_sunday - timedelta(days=14)).month
        ):
            break
        second_sunday += timedelta(days=7)
    assert next(cron) == second_sunday
