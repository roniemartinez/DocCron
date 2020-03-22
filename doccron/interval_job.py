# !/usr/bin/env python
# __author__ = "Ronie Martinez"
# __copyright__ = "Copyright 2020, Ronie Martinez"
# __credits__ = ["Ronie Martinez"]
# __maintainer__ = "Ronie Martinez"
# __email__ = "ronmarti18@gmail.com"
from datetime import datetime, timedelta, tzinfo

from dateutil.tz import tzlocal


class IntervalJob(object):
    def __init__(
        self, interval: timedelta, quartz: bool = False, timezone: tzinfo = tzlocal()
    ):
        self._interval = interval
        self._quartz = quartz
        self._timezone = timezone
        self._next_schedule = datetime.now(tz=self._timezone).replace(microsecond=0)

    def __iter__(self):
        return self

    def __next__(self):
        self._next_schedule += self._interval
        return self._next_schedule
