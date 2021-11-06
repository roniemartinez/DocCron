from datetime import datetime, timedelta
from typing import Any, Iterable, Optional, Union

from dateutil.tz import tzfile, tzlocal, tzwin  # type: ignore

from doccron.cron_job import CronJob
from doccron.exceptions import InvalidSchedule
from doccron.interval_job import IntervalJob


class CronTable:
    def __init__(self, jobs: Iterable[Any], quartz: bool = False):
        self._jobs = {}
        self._previous_schedule: Optional[datetime] = None
        self._timezone: Union[tzlocal, tzfile] = tzlocal()
        job: Union[IntervalJob, CronJob]
        for j in jobs:
            if isinstance(j, tzfile):
                self._timezone = j
                continue
            try:
                if isinstance(j, tzwin):
                    self._timezone = j
                    continue
            except TypeError:
                pass
            if isinstance(j, timedelta):
                job = IntervalJob(j, quartz, timezone=self._timezone)
            else:
                try:
                    job = CronJob(j, quartz=quartz, timezone=self._timezone)
                except ValueError:
                    raise InvalidSchedule
            self._jobs[job] = next(job)

    def __iter__(self) -> "CronTable":
        return self

    def __next__(self) -> datetime:
        while True:
            if not len(self._jobs):
                return  # type: ignore
            job, next_schedule = sorted(self._jobs.items(), key=lambda x: x[1])[0]
            if next_schedule is None:
                del self._jobs[job]
                return  # type: ignore
            self._jobs[job] = next(job)
            if self._previous_schedule and next_schedule <= self._previous_schedule:
                continue
            self._previous_schedule = next_schedule
            return next_schedule
