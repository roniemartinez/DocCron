from datetime import datetime, timedelta

from dateutil.tz import tzlocal

import doccron


def bar() -> None:
    pass


def test_non_infinite_jobs() -> None:
    next_minute = datetime.now(tz=tzlocal()).replace(second=0, microsecond=0) + timedelta(minutes=1)
    bar.__doc__ = """
    /etc/crontab::

        {} {} {} {} * {}
    """.format(
        next_minute.minute,
        next_minute.hour,
        next_minute.day,
        next_minute.month,
        next_minute.year,
    )
    jobs_found = False
    for next_schedule, function_object in doccron.run_jobs(simulate=True):
        assert next_schedule == datetime.now(tz=tzlocal()).replace(second=0, microsecond=0) + timedelta(minutes=1)
        jobs_found = True
    assert jobs_found
