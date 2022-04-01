from datetime import datetime
from unittest import TestCase
from src.data import Location, Observation, SunData
from src.capture import run


class TestCapture(TestCase):

    def test_capture_does_nothing(self):
        run(Observation(datetime.now(), Location(10, 10),
                        SunData(datetime.now(), datetime.now())))
