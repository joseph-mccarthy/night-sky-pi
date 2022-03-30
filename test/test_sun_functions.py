from datetime import datetime
from unittest import TestCase
from src.data import Location
from src.sun_functions import get_rise_and_set

class TestSunFunctions(TestCase):
    
    
    def test_sun_function(self)->None:
        date = datetime(2022,3,30)
        
        sun = get_rise_and_set(date,Location(10,10))
        
        self.assertIsNotNone(sun.sunrise)
        self.assertIsNotNone(sun.sunset)
        self.assertAlmostEqual(sun.sunrise,datetime(2022,3,30,5,19))
        self.assertAlmostEqual(sun.sunset,datetime(2022,3,30,17,31))

        
        