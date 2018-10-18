#!/usr/bin/env python
# __author__ = "Ronie Martinez"
# __copyright__ = "Copyright 2018, Ronie Martinez"
# __credits__ = ["Ronie Martinez"]
# __maintainer__ = "Ronie Martinez"
# __email__ = "ronmarti18@gmail.com"
# __status__ = "Development"
from datetime import datetime, timedelta


class Job(object):

    def __init__(self, jobs):
        minute, hour, day, month, weekday = jobs
        if minute == '*':
            self.minute = list(range(0, 60))
        else:
            self.minute = []
        if hour == '*':
            self.hour = list(range(0, 24))
        else:
            self.hour = []
        if day == '*':
            self.day = list(range(0, 32))
        else:
            self.day = []
        if month == '*':
            self.month = list(range(1, 13))
        else:
            self.month = []
        if weekday == '*':
            self.weekday = list(range(1, 8))
        else:
            self.weekday = []
        self.previous_datetime = datetime.now()

    def __iter__(self):
        return self

    def __next__(self):
        next_datetime = self.previous_datetime.replace(second=0, microsecond=0) + timedelta(minutes=1)
        while True:
            if next_datetime.month in self.month and \
                    next_datetime.day in self.day and \
                    next_datetime.hour in self.hour and \
                    next_datetime.minute in self.minute and \
                    next_datetime.isoweekday() in self.weekday:
                self.previous_datetime = next_datetime
                return next_datetime
            else:
                next_datetime += timedelta(minutes=1)

    next = __next__


class CronTable(object):

    def __init__(self, jobs):
        self.jobs = [Job(job) for job in jobs]
        self.schedules = []

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.jobs[0])

    next = __next__


def tokenize(jobs: str):
    for jobs in jobs.splitlines():
        yield jobs.split(None, 5)


def cron(jobs):
    return CronTable(tokenize(jobs))
