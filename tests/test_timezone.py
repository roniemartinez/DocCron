#!/usr/bin/env python
# __author__ = "Ronie Martinez"
# __copyright__ = "Copyright 2018-2020, Ronie Martinez"
# __credits__ = ["Ronie Martinez"]
# __maintainer__ = "Ronie Martinez"
# __email__ = "ronmarti18@gmail.com"
from collections.abc import Iterator
from datetime import datetime, timedelta

from dateutil.tz import tzlocal

import doccron


def test_single_timezone():
    current_datetime = datetime.now(tz=tzlocal()).replace(
        minute=0, second=0, microsecond=0
    )
    cron = doccron.cron(
        """CRON_TZ=Japan
    0 * * * *"""
    )
    assert isinstance(cron, Iterator)

    for i in range(1, 6):
        next_schedule = next(cron)
        assert isinstance(next_schedule, datetime)
        assert next_schedule == current_datetime + timedelta(hours=i)


def test_multiple_timezone():
    current_datetime = datetime.now(tz=tzlocal()).replace(
        minute=0, second=0, microsecond=0
    )

    cron = doccron.cron(
        """CRON_TZ=Asia/Manila
    0 */2 * * *
    CRON_TZ=UTC
    0 1-23/2 * * *"""
    )
    assert isinstance(cron, Iterator)

    for i in range(1, 6):
        next_schedule = next(cron)
        assert isinstance(next_schedule, datetime)
        assert next_schedule == current_datetime + timedelta(hours=i)
