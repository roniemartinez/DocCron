from datetime import datetime

from freezegun import freeze_time

import doccron


def foo() -> None:
    """
    This function prints "foo"

        /etc/crontab::

        * * * * * 2021
        * * * * * 2020

    :returns: None
    """
    print("foo")


def bar() -> None:
    """
    /etc/crontab::

        * * * * * 2021
        * * * * * 2020
    This should not be added
    """
    print("bar")


def baz() -> None:
    """
    * * * * * 2021
    * * * * * 2020
    """
    print("baz")


@freeze_time("2020-01-01")
def test_find_functions_with_docstrings() -> None:
    run_count = 0
    jobs_found = False
    for next_schedule, function_object in doccron.run_jobs(simulate=True):
        jobs_found = True
        assert isinstance(next_schedule, datetime)
        assert function_object.__name__ in ("foo", "bar")
        assert function_object.__name__ != "baz"
        run_count += 1
        if run_count == 5:
            break
    assert jobs_found
