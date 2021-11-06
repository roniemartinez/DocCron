from datetime import datetime, timedelta

import doccron


def test_steps() -> None:
    cron = doccron.cron("*/15 */6 1,15,31 * *")
    next_datetime = datetime.now().replace(minute=0, second=0, microsecond=0)
    while True:
        if (
            next_datetime.day in [1, 15, 31]
            and next_datetime.hour in [0, 6, 12, 18]
            and next_datetime.minute in [0, 15, 30, 45]
        ):
            break
        next_datetime += timedelta(minutes=15)
    next_schedule = next(cron)  # type: datetime
    assert isinstance(next_schedule, datetime)
    assert next_schedule.day in [1, 15, 31]
    assert next_schedule.hour in [0, 6, 12, 18]
    assert next_schedule.minute in [0, 15, 30, 45]
