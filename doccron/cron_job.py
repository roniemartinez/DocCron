#!/usr/bin/env python
# __author__ = "Ronie Martinez"
# __copyright__ = "Copyright 2018-2020, Ronie Martinez"
# __credits__ = ["Ronie Martinez"]
# __maintainer__ = "Ronie Martinez"
# __email__ = "ronmarti18@gmail.com"
import itertools
from calendar import monthrange
from datetime import MAXYEAR, datetime, timedelta, tzinfo
from typing import Any, Iterator, List, Tuple, Union

from dateutil.tz import tzlocal

from doccron.timezone import localize

MONTH_NAMES = [
    "jan",
    "feb",
    "mar",
    "apr",
    "may",
    "jun",
    "jul",
    "aug",
    "sep",
    "oct",
    "nov",
    "dec",
]
WEEKDAY_NAMES = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]


def _parse_steps(item: str) -> Tuple[str, int]:
    try:
        item, step = item.split("/", 1)
        return item, int(step)
    except ValueError:
        return item, 1


def _odometer(
    odometer: Iterator[Tuple[Any, ...]], seconds: list, timezone: tzinfo
) -> Iterator[Tuple[Any, ...]]:
    current_time_tuple = tuple(datetime.now(tz=timezone).timetuple())[:6]
    for i in odometer:
        try:
            if i < current_time_tuple[:5]:
                continue
        except TypeError:  # pragma: no cover
            pass
        for second in seconds:
            try:
                if i + (second,) < current_time_tuple:
                    continue
            except TypeError:  # pragma: no cover
                pass
            yield i + (second,)


class CronJob(object):
    def __init__(self, job: list, quartz: bool = False, timezone: tzinfo = tzlocal()):
        self.seconds: List[int] = [] if quartz else [0]
        self.minutes: List[int] = []
        self.hours: List[int] = []
        self.days: List[Union[int, str]] = []
        self.weekdays: List[Union[int, str]] = []
        self.months: List[int] = []
        self.years: List[int] = []
        self.timezone = timezone
        self._quartz = quartz
        try:
            if self._quartz:
                second, minute, hour, day, month, weekday, year = job
            else:
                minute, hour, day, month, weekday, year = job
        except ValueError:
            if self._quartz:
                second, minute, hour, day, month, weekday = job
            else:
                minute, hour, day, month, weekday = job
            year = "*"

        if self._quartz:
            # noinspection PyUnboundLocalVariable
            self._parse_second(second)
        self._parse_minute(minute)
        self._parse_hour(hour)
        self._parse_day(day)
        self._parse_month(month)
        self._parse_weekday(weekday)
        self._parse_year(year)

        self.iterator = _odometer(
            itertools.product(
                self.years, self.months, self.days, self.hours, self.minutes
            ),
            self.seconds,
            self.timezone,
        )

    def _parse_second(self, second) -> None:
        seconds, step = _parse_steps(second)
        if seconds == "*":
            self.seconds = list(range(0, 60))
        else:
            for m in seconds.split(","):
                if m.isdigit():
                    self.seconds.append(int(m))
                else:
                    start, end = m.split("-", 1)
                    self.seconds += list(range(int(start), int(end) + 1))
        self.seconds = sorted(self.seconds)[::step]

    def _parse_minute(self, minute) -> None:
        minutes, step = _parse_steps(minute)
        if minutes == "*":
            self.minutes = list(range(0, 60))
        else:
            for m in minutes.split(","):
                if m.isdigit():
                    self.minutes.append(int(m))
                else:
                    start, end = m.split("-", 1)
                    self.minutes += list(range(int(start), int(end) + 1))
        self.minutes = sorted(self.minutes)[::step]

    def _parse_hour(self, hour) -> None:
        hours, step = _parse_steps(hour)
        if hours == "*":
            self.hours = list(range(0, 24))
        else:
            for m in hours.split(","):
                if m.isdigit():
                    self.hours.append(int(m))
                else:
                    start, end = m.split("-", 1)
                    self.hours += list(range(int(start), int(end) + 1))
        self.hours = sorted(self.hours)[::step]

    def _parse_day(self, day) -> None:
        days, step = _parse_steps(day)
        if days == "*":
            self.days = list(range(1, 32))
        elif days == "L":
            self.days = [day]
        elif days.endswith("W") and days[:-1].isdigit():
            self.days = [days]
        else:
            for m in days.split(","):
                if m.isdigit():
                    self.days.append(int(m))
                else:
                    start, end = m.split("-", 1)
                    self.days += list(range(int(start), int(end) + 1))
        self.days = sorted(self.days)[::step]

    def _parse_weekday(self, weekday) -> None:
        weekdays, step = _parse_steps(weekday)
        if weekdays == "*":
            self.weekdays = list(range(1, 8))
        elif weekdays.endswith("L") and weekdays[:-1].isdigit():
            self.weekdays = [weekdays]
        elif "#" in weekdays and all(x.isdigit() for x in weekdays.split("#")):
            self.weekdays = [weekdays]
        else:
            for w in weekdays.split(","):
                if w.isdigit():
                    i = int(w)
                    self.weekdays.append(7 if i == 0 else i)  # sunday can be 0 in cron
                elif w.isalpha():
                    self.weekdays.append(WEEKDAY_NAMES.index(w.lower()) + 1)
                else:
                    start, end = w.split("-", 1)
                    start = (
                        start
                        if start.isdigit()
                        else str(WEEKDAY_NAMES.index(start.lower()) + 1)
                    )
                    end = (
                        end
                        if end.isdigit()
                        else str(WEEKDAY_NAMES.index(end.lower()) + 1)
                    )
                    self.weekdays += list(range(int(start), int(end) + 1))
        self.weekdays = sorted(self.weekdays)[::step]

    def _parse_month(self, month) -> None:
        months, step = _parse_steps(month)
        if months == "*":
            self.months = list(range(1, 13))
        else:
            for w in months.split(","):
                if w.isdigit():
                    self.months.append(int(w))
                elif w.isalpha():
                    self.months.append(MONTH_NAMES.index(w.lower()) + 1)
                else:
                    start, end = w.split("-", 1)
                    start = (
                        start
                        if start.isdigit()
                        else str(MONTH_NAMES.index(start.lower()) + 1)
                    )
                    end = (
                        end
                        if end.isdigit()
                        else str(MONTH_NAMES.index(end.lower()) + 1)
                    )
                    self.months += list(range(int(start), int(end) + 1))
        self.months = sorted(self.months)[::step]

    def _parse_year(self, year) -> None:
        years, step = _parse_steps(year)
        if years == "*":
            self.years = list(range(datetime.now(tz=self.timezone).year, MAXYEAR))
        else:
            for m in years.split(","):
                if m.isdigit():
                    self.years.append(int(m))
                else:
                    start, end = m.split("-", 1)
                    self.years += list(range(int(start), int(end) + 1))
        self.years = sorted(self.years)[::step]

    def __iter__(self):
        return self

    def __next__(self):
        for i in self.iterator:
            try:
                try:
                    next_datetime = localize(datetime(*i), self.timezone)
                    if next_datetime <= datetime.now(tz=self.timezone):
                        continue
                    weekday = self.weekdays[0]
                    if len(self.weekdays) == 1 and isinstance(weekday, str):
                        if (
                            weekday[-1] == "L"
                            and next_datetime.isoweekday() == int(weekday[:-1])
                            and (next_datetime + timedelta(days=7)).month
                            != next_datetime.month
                        ):
                            return next_datetime
                        elif "#" in weekday:
                            weekday, order = map(int, weekday.split("#"))
                            weekday = 7 if weekday == 0 else weekday
                            if next_datetime.isoweekday() != weekday:
                                continue
                            if (
                                next_datetime.month
                                == (
                                    next_datetime - timedelta(days=7 * (order - 1))
                                ).month
                                and next_datetime.month
                                != (next_datetime - timedelta(days=7 * order)).month
                            ):
                                return next_datetime
                            continue
                    if next_datetime.isoweekday() in self.weekdays:
                        return next_datetime
                except TypeError:  # non-standard characters
                    year, month, day, hour, minute, second = i
                    if day == "L":
                        day = monthrange(year, month)[1]
                        next_datetime = localize(
                            datetime(year, month, day, hour, minute, second),
                            self.timezone,
                        )
                        if (
                            next_datetime > datetime.now(tz=self.timezone)
                            and next_datetime.isoweekday() in self.weekdays
                        ):
                            return next_datetime
                    elif day[-1] == "W":
                        next_datetime = localize(
                            datetime(year, month, int(day[:-1]), hour, minute, second),
                            self.timezone,
                        )
                        if (
                            next_datetime <= datetime.now(tz=self.timezone)
                            or next_datetime.isoweekday() not in self.weekdays
                        ):
                            continue
                        if next_datetime.isoweekday() == 6:
                            if next_datetime.day == 1:
                                next_datetime += timedelta(days=2)
                            elif (next_datetime - timedelta(days=1)) > datetime.now(
                                tz=self.timezone
                            ):
                                next_datetime -= timedelta(days=1)
                        elif next_datetime.isoweekday() in (0, 7):
                            next_datetime += timedelta(days=1)
                        return next_datetime
            except ValueError:
                continue
