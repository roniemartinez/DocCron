#!/usr/bin/env python
# __author__ = "Ronie Martinez"
# __copyright__ = "Copyright 2018, Ronie Martinez"
# __credits__ = ["Ronie Martinez"]
# __maintainer__ = "Ronie Martinez"
# __email__ = "ronmarti18@gmail.com"
# __status__ = "Development"
from collections import Iterable
from datetime import datetime, timedelta

import doccron


def test_tokenizer():
    assert [['*'] * 5] == list(doccron.tokenize('* * * * *'))
    assert [['*'] * 5] == list(doccron.tokenize('*  * * * *'))
    assert [['*'] * 5] * 2 == list(doccron.tokenize('* * * * *\n* * * * *'))
    assert [['*'] * 5] * 2 == list(doccron.tokenize('''* * * * *
    * * * * *'''))


def test_schedule():
    current_datetime = datetime.now().replace(second=0, microsecond=0)
    cron = doccron.cron('* * * * *')
    assert isinstance(cron, doccron.CronTable)
    assert isinstance(cron, Iterable)

    for i in range(1, 6):
        next_schedule = next(cron)
        assert isinstance(next_schedule, datetime)
        assert next_schedule == current_datetime + timedelta(minutes=i)
