from datetime import datetime
from unittest import TestCase
from src.capture import capture
from src.data import Location, Observation, SunData

class TestCapture(TestCase):
    
    def test_capture_does_nothing(self):
        capture(Observation(datetime.now(),Location(10,10),SunData(datetime.now(),datetime.now())))