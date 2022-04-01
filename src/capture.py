from data import Observation


def run(observation: Observation) -> None:
    print(
        f'Capture from {observation.sun.sunset} to {observation.sun.sunrise}')
