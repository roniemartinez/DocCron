#!/usr/bin/env python
# __author__ = "Ronie Martinez"
# __copyright__ = "Copyright 2018, Ronie Martinez"
# __credits__ = ["Ronie Martinez"]
# __maintainer__ = "Ronie Martinez"
# __email__ = "ronmarti18@gmail.com"
# __status__ = "Production"
from datetime import datetime, timedelta

import doccron


def test_steps():
    cron = doccron.cron('*/15 */6 1,15,31 * *')
    next_datetime = datetime.now().replace(minute=0, second=0, microsecond=0)
    while True:
        if next_datetime.day in [1, 15, 31] and next_datetime.hour in [0, 6, 12, 18] and \
                next_datetime.minute in [0, 15, 30, 45]:
            break
        next_datetime += timedelta(minutes=15)
    next_schedule = next(cron)  # type: datetime
    assert isinstance(next_schedule, datetime)
    assert next_schedule.isoweekday() in [1, 2, 3, 4, 5]
