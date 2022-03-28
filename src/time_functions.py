from datetime import datetime, timedelta

def get_today() -> datetime:
    return datetime.now()

def get_tomorrow() -> datetime:
    return datetime.now() + timedelta(1)

def get_yesterday() -> datetime:
    return datetime.now() - timedelta(1)

def get_dates()->tuple():
    return (get_yesterday(),get_today(),get_tomorrow())