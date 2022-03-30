from datetime import datetime
from unittest import TestCase
from unittest.mock import patch
import src.time_functions as time

class TestTimeFunctions(TestCase):
    
    @patch('src.time_functions._get_now', return_value=datetime(2022,2,1))
    def test_get_today(self,mock_datetime):
        today = time.get_today()
        self.assertEqual(today,datetime(2022,2,1))
        
    @patch('src.time_functions._get_now', return_value=datetime(2022,2,1))
    def test_get_yesterday(self,mock_datetime):
        yesterday = time.get_yesterday()
        self.assertEqual(yesterday,datetime(2022,1,31))
        
    @patch('src.time_functions._get_now', return_value=datetime(2022,2,1))
    def test_get_tomorrow(self,mock_datetime):
        tomorrow = time.get_tomorrow()
        self.assertEqual(tomorrow,datetime(2022,2,2))
        
    @patch('src.time_functions._get_now', return_value=datetime(2022,2,1))
    def test_get_dates(self,mock_datetime):
        yesterday,today,tomorrow = time.get_dates()
        self.assertEqual(yesterday,datetime(2022,1,31))
        self.assertEqual(today,datetime(2022,2,1))
        self.assertEqual(tomorrow,datetime(2022,2,2))
        
    def test_get_now(self):
        self.assertEqual(time._get_now().day,datetime.now().day)