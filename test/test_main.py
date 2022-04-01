from datetime import datetime
from unittest import TestCase
from unittest.mock import PropertyMock, patch
from src.main import Main
from src.data import SunData


class TestMain(TestCase):

    @patch('src.main.time._get_now', return_value=datetime(2022, 2, 1, 15, 30))
    @patch('src.main.sun.get_rise_and_set', return_value=SunData(datetime(2022, 2, 1, 5, 30), datetime(2022, 2, 1, 18, 30)))
    @patch('src.main.Main')
    @patch('src.main.capture')
    def test_time_to_process(self, capture, mock_time, mock_sun, main_mock):
        sentinel = PropertyMock(side_effect=[True, False])
        Main.RUNNING = sentinel
        application: Main = Main(10, 10)
        application.run()
        self.assertFalse(capture.run.called)
