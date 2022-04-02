from datetime import datetime
from unittest import TestCase
from unittest.mock import PropertyMock, patch
from src.main import Main
from src.data import SunData


class TestMain(TestCase):

    yesterday_sun = SunData(datetime(2022, 1, 31, 5, 30).replace(tzinfo=None),
                            datetime(2022, 1, 31, 18, 30).replace(tzinfo=None))

    today_sun = SunData(datetime(2022, 2, 1, 5, 30).replace(tzinfo=None),
                        datetime(2022, 2, 1, 18, 30).replace(tzinfo=None))
    tomorrow_sun = SunData(datetime(2022, 2, 2, 5, 30).replace(tzinfo=None),
                           datetime(2022, 2, 2, 18, 30).replace(tzinfo=None))

    @patch('src.main.sun.get_rise_and_set', return_value=SunData(datetime(2022, 2, 1, 5, 30), datetime(2022, 2, 1, 18, 30)))
    @patch('src.main.time._get_now', return_value=datetime(2022, 2, 1, 15, 30))
    @patch('src.main.capture')
    def test_time_to_process(self, mock_sun, main_mock, capture):
        Main.RUNNING = PropertyMock(side_effect=[True, False])
        application: Main = Main(10, 10)
        application.run()
        self.assertFalse(capture.run.called)

    @patch('src.main.capture')
    @patch('src.main.time._get_now', return_value=datetime(2022, 2, 1, 20, 30).replace(tzinfo=None))
    @patch('src.main.sun.get_rise_and_set', side_effect=[yesterday_sun, today_sun, tomorrow_sun])
    def test_after_sunset_today(self, mock_sun, mock_time, capture):

        Main.RUNNING = PropertyMock(side_effect=[True, False])
        application: Main = Main(10, 10)
        application.run()
        assert capture.run.called
        self.assertEqual(
            capture.run.call_args_list[0].args[0].sun.sunset.day, 1)
        self.assertEqual(
            capture.run.call_args_list[0].args[0].sun.sunrise.day, 2)

    @patch('src.main.capture')
    @patch('src.main.time._get_now', return_value=datetime(2022, 2, 1, 2, 30).replace(tzinfo=None))
    @patch('src.main.sun.get_rise_and_set', side_effect=[yesterday_sun, today_sun, tomorrow_sun])
    def test_after_sunset_yesterday_and_before_sunrise_todat(self, mock_sun, mock_time, capture):

        Main.RUNNING = PropertyMock(side_effect=[True, False])
        application: Main = Main(10, 10)
        application.run()
        assert capture.run.called
        self.assertEqual(
            capture.run.call_args_list[0].args[0].sun.sunset.day, 31)
        self.assertEqual(
            capture.run.call_args_list[0].args[0].sun.sunrise.day, 1)
