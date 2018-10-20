#!/usr/bin/env python
# __author__ = "Ronie Martinez"
# __copyright__ = "Copyright 2018, Ronie Martinez"
# __credits__ = ["Ronie Martinez"]
# __maintainer__ = "Ronie Martinez"
# __email__ = "ronmarti18@gmail.com"
# __status__ = "Production"
from datetime import datetime, timedelta

import doccron

current_minute = datetime.now().replace(second=0, microsecond=0)
next_minute = current_minute + timedelta(minutes=1)


def foo():
    "{} {} {} {} * {}".format(current_minute.minute, current_minute.hour, current_minute.day, current_minute.month,
                              current_minute.year)
    pass


def bar():
    "{} {} {} {} * {}".format(next_minute.minute, next_minute.hour, next_minute.day, next_minute.month,
                              next_minute.year)
    pass


def test_non_infinite_jobs():
    for next_schedule, function_object in doccron.run_jobs(simulate=True):
        assert next_schedule == datetime.now().replace(second=0, microsecond=0) + timedelta(minutes=1)
