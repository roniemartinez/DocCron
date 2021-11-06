from datetime import datetime, tzinfo

from dateutil.tz import tzlocal


def localize(dt: datetime, timezone: tzinfo = tzlocal()) -> datetime:
    return dt.replace(tzinfo=timezone)
