#!/usr/bin/env python
# __author__ = "Ronie Martinez"
# __copyright__ = "Copyright 2018, Ronie Martinez"
# __credits__ = ["Ronie Martinez"]
# __maintainer__ = "Ronie Martinez"
# __email__ = "ronmarti18@gmail.com"
# __status__ = "Production"
from doccron.job import Job


class CronTable(object):

    # noinspection PyShadowingNames
    def __init__(self, jobs):
        self._jobs = {}
        self._previous_schedule = None
        for j in jobs:
            job = Job(j)
            try:
                self._jobs[job] = next(job)
            except StopIteration:
                pass

    def __iter__(self):
        return self

    # noinspection PyShadowingNames
    def __next__(self):
        if not len(self._jobs):
            return
        job, next_schedule = sorted(self._jobs.items(), key=lambda x: x[1])[0]
        try:
            self._jobs[job] = next(job)
        except StopIteration:
            del self._jobs[job]
        if self._previous_schedule and next_schedule <= self._previous_schedule:
            return next(self)
        self._previous_schedule = next_schedule
        return next_schedule

    next = __next__
