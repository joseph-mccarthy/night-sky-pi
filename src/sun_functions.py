from suntime import Sun, SunTimeException
from datetime import datetime
from data import Location,SunData


def get_rise_and_set(date: datetime, location:Location) -> SunData:
    sun = Sun(location.latitude, location.longitude)
    sunrise = sun.get_sunrise_time(date).replace(tzinfo=None)
    sunset = sun.get_sunset_time(date).replace(tzinfo=None)
    return SunData(sunrise,sunset)
