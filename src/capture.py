from datetime import datetime


def capture(obs_date: datetime, location: tuple, duration: tuple) -> None:
    sunset, sunrise = duration
    print(f'Capture from {sunset} to {sunrise}')
