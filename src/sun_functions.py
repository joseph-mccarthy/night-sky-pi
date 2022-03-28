from suntime import Sun, SunTimeException
from datetime import datetime

def get_rise_and_set(date:datetime,coorindates:tuple()) -> tuple():
    latitude, longitude = coorindates
    sun = Sun(latitude, longitude)
    sr = sun.get_sunrise_time(date).replace(tzinfo=None)
    ss = sun.get_sunset_time(date).replace(tzinfo=None)
    return (sr,ss)