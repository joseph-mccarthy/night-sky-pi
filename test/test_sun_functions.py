from datetime import datetime
from unittest import TestCase
from src.sun_functions import get_rise_and_set as undertest


class TestSunFunctions(TestCase):
    
    
    def test_sun_function(self)->None:
        coord = (10,10)
        date = datetime(2022,3,30)
        
        sunrise, sunset = undertest(date,coord)
        
        self.assertIsNotNone(sunrise)
        self.assertIsNotNone(sunset)
        self.assertAlmostEqual(sunrise,datetime(2022,3,30,5,19))
        self.assertAlmostEqual(sunset,datetime(2022,3,30,17,31))

        
        