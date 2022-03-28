from suntime import Sun, SunTimeException
from datetime import datetime

def get_rise_and_set(date:datetime,coorindates:tuple()) -> tuple():
    latitude, longitude = coorindates
    sun = Sun(latitude, longitude)
    abd_sr = sun.get_sunrise_time(date).replace(tzinfo=None)
    abd_ss = sun.get_sunset_time(date).replace(tzinfo=None)
    return (abd_sr,abd_ss)