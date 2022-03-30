from data import Observation


def capture(observation:Observation) -> None:
    print(f'Capture from {observation.sun.sunset} to {observation.sun.sunrise}')
