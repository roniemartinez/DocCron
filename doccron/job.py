#!/usr/bin/env python
# __author__ = "Ronie Martinez"
# __copyright__ = "Copyright 2018, Ronie Martinez"
# __credits__ = ["Ronie Martinez"]
# __maintainer__ = "Ronie Martinez"
# __email__ = "ronmarti18@gmail.com"
# __status__ = "Production"

import itertools
from datetime import datetime, MAXYEAR

MONTH_NAMES = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
WEEKDAY_NAMES = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']


def _parse_steps(item):
    try:
        item, step = item.split('/', 1)
        return item, int(step)
    except ValueError:
        return item, 1


class Job(object):

    def __init__(self, jobs):
        self.previous_datetime = None
        self.minutes = []
        self.hours = []
        self.days = []
        self.weekdays = []
        self.months = []
        self.years = []
        try:
            minute, hour, day, month, weekday, year = jobs
        except ValueError:
            minute, hour, day, month, weekday = jobs
            year = '*'

        self.base_datetime = datetime.now().replace(second=0, microsecond=0)

        self._parse_minute(minute)
        self._parse_hour(hour)
        self._parse_day(day)
        self._parse_month(month)
        self._parse_weekday(weekday)
        self._parse_year(year)

        self.iterator = itertools.product(self.years, self.months, self.days, self.hours, self.minutes)

    def _parse_minute(self, minute):
        minutes, step = _parse_steps(minute)
        if minutes == '*':
            self.minutes = list(range(0, 60))
        else:
            for m in minutes.split(','):
                if m.isdigit():
                    self.minutes.append(int(m))
                else:
                    start, end = m.split('-', 1)
                    self.minutes += list(range(int(start), int(end) + 1))
        self.minutes = self.minutes[::step]

    def _parse_hour(self, hour):
        hours, step = _parse_steps(hour)
        if hours == '*':
            self.hours = list(range(0, 24))
        else:
            for m in hours.split(','):
                if m.isdigit():
                    self.hours.append(int(m))
                else:
                    start, end = m.split('-', 1)
                    self.hours += list(range(int(start), int(end) + 1))
        self.hours = self.hours[::step]

    def _parse_day(self, day):
        days, step = _parse_steps(day)
        if days == '*':
            self.days = list(range(1, 32))
        else:
            for m in days.split(','):
                if m.isdigit():
                    self.days.append(int(m))
                else:
                    start, end = m.split('-', 1)
                    self.days += list(range(int(start), int(end) + 1))
        self.days = self.days[::step]

    def _parse_weekday(self, weekday):
        weekdays, step = _parse_steps(weekday)
        if weekdays == '*':
            self.weekdays = list(range(1, 8))
        else:
            for w in weekdays.split(','):
                if w.isdigit():
                    i = int(w)
                    self.weekdays.append(7 if i == 0 else i)  # sunday can be 0 in cron
                elif w.isalpha():
                    self.weekdays.append(WEEKDAY_NAMES.index(w.lower()) + 1)
                else:
                    start, end = w.split('-', 1)
                    start = start if start.isdigit() else WEEKDAY_NAMES.index(start.lower()) + 1
                    end = end if end.isdigit() else WEEKDAY_NAMES.index(end.lower()) + 1
                    self.weekdays += list(range(int(start), int(end) + 1))
        self.weekdays = self.weekdays[::step]

    def _parse_month(self, month):
        months, step = _parse_steps(month)
        if months == '*':
            self.months = list(range(1, 13))
        else:
            for w in months.split(','):
                if w.isdigit():
                    self.months.append(int(w))
                elif w.isalpha():
                    self.months.append(MONTH_NAMES.index(w.lower()) + 1)
                else:
                    start, end = w.split('-', 1)
                    start = start if start.isdigit() else MONTH_NAMES.index(start.lower()) + 1
                    end = end if end.isdigit() else MONTH_NAMES.index(end.lower()) + 1
                    self.months += list(range(int(start), int(end) + 1))
        self.months = self.months[::step]

    def _parse_year(self, year):
        years, step = _parse_steps(year)
        if years == '*':
            self.years = list(range(self.base_datetime.year, MAXYEAR))
        else:
            for m in years.split(','):
                if m.isdigit():
                    self.years.append(int(m))
                else:
                    start, end = m.split('-', 1)
                    self.years += list(range(int(start), int(end) + 1))
        self.years = self.years[::step]

    def __iter__(self):
        return self

    def __next__(self):
        for i in self.iterator:
            try:
                next_datetime = datetime(*i)
                if next_datetime <= datetime.now():
                    continue
                if next_datetime.isoweekday() in self.weekdays:
                    if self.previous_datetime and next_datetime <= self.previous_datetime:
                        self.previous_datetime = next_datetime
                        continue
                    self.previous_datetime = next_datetime
                    return next_datetime
            except ValueError:
                continue

    next = __next__
