from datetime import datetime, timedelta

def _get_now() -> datetime:
    return datetime.now()

def get_today() -> datetime:
    return _get_now()


def get_tomorrow() -> datetime:
    return _get_now() + timedelta(1)


def get_yesterday() -> datetime:
    return _get_now() - timedelta(1)


def get_dates() -> tuple():
    return (get_yesterday(), get_today(), get_tomorrow())
