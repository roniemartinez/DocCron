from datetime import datetime, timedelta, tzinfo

from dateutil.tz import tzlocal


class IntervalJob:
    def __init__(self, interval: timedelta, quartz: bool = False, timezone: tzinfo = tzlocal()):
        self._interval = interval
        self._quartz = quartz
        self._timezone = timezone
        self._next_schedule: datetime = datetime.now(tz=self._timezone).replace(microsecond=0)

    def __iter__(self) -> "IntervalJob":
        return self

    def __next__(self) -> datetime:
        self._next_schedule += self._interval
        return self._next_schedule
