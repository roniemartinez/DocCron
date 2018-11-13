#!/usr/bin/env python
# __author__ = "Ronie Martinez"
# __copyright__ = "Copyright 2018, Ronie Martinez"
# __credits__ = ["Ronie Martinez"]
# __maintainer__ = "Ronie Martinez"
# __email__ = "ronmarti18@gmail.com"
# __status__ = "Development"
from datetime import datetime, timedelta

import doccron


def bar():
    pass


def test_non_infinite_jobs():
    next_minute = datetime.now().replace(second=0, microsecond=0) + timedelta(minutes=1)
    bar.__doc__ = """
    /etc/crontab::
    
        {} {} {} {} * {}
    """.format(next_minute.minute, next_minute.hour, next_minute.day, next_minute.month, next_minute.year)
    jobs_found = False
    for next_schedule, function_object in doccron.run_jobs(simulate=True):
        assert next_schedule == datetime.now().replace(second=0, microsecond=0) + timedelta(minutes=1)
        jobs_found = True
    assert jobs_found
