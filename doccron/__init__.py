#!/usr/bin/env python
# __author__ = "Ronie Martinez"
# __copyright__ = "Copyright 2018, Ronie Martinez"
# __credits__ = ["Ronie Martinez"]
# __maintainer__ = "Ronie Martinez"
# __email__ = "ronmarti18@gmail.com"
# __status__ = "Development"
import itertools
from datetime import datetime


def make_first(items, item):
    index = items.index(item)
    return items[index:] + items[:index]


class Job(object):

    def __init__(self, jobs):
        try:
            minute, hour, day, month, weekday, year = jobs
        except ValueError:
            minute, hour, day, month, weekday = jobs
            year = '*'

        current_datetime = datetime.now().replace(second=0, microsecond=0)

        if minute == '*':
            self.minutes = make_first(list(range(0, 60)), current_datetime.minute)
        else:
            self.minutes = list(map(int, minute.split(',')))
        if hour == '*':
            self.hours = make_first(list(range(0, 24)), current_datetime.hour)
        else:
            self.hours = list(map(int, hour.split(',')))
        if day == '*':
            self.days = make_first(list(range(1, 32)), current_datetime.day)
        else:
            self.days = list(map(int, day.split(',')))
        if month == '*':
            self.months = make_first(list(range(1, 13)), current_datetime.month)
        else:
            self.months = list(map(int, month.split(',')))
        if weekday == '*':
            self.weekdays = list(range(1, 8))
        else:
            self.weekdays = list(map(int, weekday.split(',')))
        if year == '*':
            self.years = list(range(current_datetime.year, 3000))
        else:
            self.years = list(map(int, year.split(',')))

        self.iterator = itertools.product(self.years, self.months, self.days, self.hours, self.minutes)

    def __iter__(self):
        return self

    def __next__(self):
        for i in self.iterator:
            try:
                next_datetime = datetime(*i)
                if next_datetime <= datetime.now():
                    continue
                if next_datetime.isoweekday() in self.weekdays:
                    return next_datetime
            except ValueError:
                continue

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
