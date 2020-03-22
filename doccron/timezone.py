#!/usr/bin/env python
# __author__ = "Ronie Martinez"
# __copyright__ = "Copyright 2019-2020, Ronie Martinez"
# __credits__ = ["Ronie Martinez"]
# __maintainer__ = "Ronie Martinez"
# __email__ = "ronmarti18@gmail.com"
from datetime import datetime

from dateutil.tz import tzlocal


def localize(dt: datetime, timezone=tzlocal()) -> datetime:
    return dt.replace(tzinfo=timezone)
