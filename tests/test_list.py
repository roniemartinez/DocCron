from datetime import datetime, timedelta

from freezegun import freeze_time

import doccron
from doccron.timezone import localize


@freeze_time("2020-01-01")
def test_year_list() -> None:
    cron = doccron.cron("45 17 7 6 * 2021,2022")
    assert next(cron) == localize(datetime(2021, 6, 7, 17, 45))
    assert next(cron) == localize(datetime(2022, 6, 7, 17, 45))


def test_lists() -> None:
    cron = doccron.cron("0,15,30,45 0,6,12,18 1,15,31 * 1,2,3,4,5 *")
    next_datetime = datetime.now().replace(minute=0, second=0, microsecond=0)
    while True:
        if (
            next_datetime.day in [1, 15, 31]
            and next_datetime.hour in [0, 6, 12, 18]
            and next_datetime.minute in [0, 15, 30, 45]
            and next_datetime.isoweekday() in range(1, 6)
        ):
            break
        next_datetime += timedelta(minutes=15)
    next_schedule = next(cron)  # type: datetime
    assert isinstance(next_schedule, datetime)
    assert next_schedule.isoweekday() in [1, 2, 3, 4, 5]
