#!/usr/bin/env python
# __author__ = "Ronie Martinez"
# __copyright__ = "Copyright 2019, Ronie Martinez"
# __credits__ = ["Ronie Martinez"]
# __maintainer__ = "Ronie Martinez"
# __email__ = "ronmarti18@gmail.com"
from tzlocal import get_localzone


def localize(datetime, timezone=get_localzone()):
    return timezone.localize(datetime, is_dst=None)
