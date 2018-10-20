#!/usr/bin/env python
# __author__ = "Ronie Martinez"
# __copyright__ = "Copyright 2018, Ronie Martinez"
# __credits__ = ["Ronie Martinez"]
# __maintainer__ = "Ronie Martinez"
# __email__ = "ronmarti18@gmail.com"
# __status__ = "Development"
from datetime import datetime

import doccron


def foo():
    """
    * * * * * 2021
    * * * * * 2020
    """
    print("foo")


def bar():
    """
    * * * * * 2021
    * * * * * 2020
    """
    print("bar")


def test_find_functions_with_docstrings():
    run_count = 0
    for next_schedule, function_object in doccron.run_jobs(simulate=True):
        assert isinstance(next_schedule, datetime)
        assert function_object.__name__ in ('foo', 'bar')
        run_count += 1
        if run_count == 5:
            break
