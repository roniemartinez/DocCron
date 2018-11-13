#!/usr/bin/env python
# __author__ = "Ronie Martinez"
# __copyright__ = "Copyright 2018, Ronie Martinez"
# __credits__ = ["Ronie Martinez"]
# __maintainer__ = "Ronie Martinez"
# __email__ = "ronmarti18@gmail.com"
# __status__ = "Production"
from datetime import datetime

import doccron


def foo():
    """
    This function prints "foo"

        /etc/crontab::

        * * * * * 2021
        * * * * * 2020

    :returns: None
    """
    print("foo")


def bar():
    """
    /etc/crontab::

        * * * * * 2021
        * * * * * 2020
    This should not be added
    """
    print("bar")


def baz():
    """
    * * * * * 2021
    * * * * * 2020
    """
    print("baz")


def test_find_functions_with_docstrings():
    run_count = 0
    jobs_found = False
    for next_schedule, function_object in doccron.run_jobs(simulate=True):
        jobs_found = True
        assert isinstance(next_schedule, datetime)
        assert function_object.__name__ in ('foo', 'bar')
        assert function_object.__name__ != 'baz'
        run_count += 1
        if run_count == 5:
            break
    assert jobs_found
