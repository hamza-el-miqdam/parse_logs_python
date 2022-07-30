from datetime import datetime, timedelta
from src.log_parser.log_parser import get_datetime_from_log_line, get_timedelta


def test_get_datetime_from_log_line():
    assert get_datetime_from_log_line({'year': '2022', 'month': '02', 'day': '01', 'hour': '12',
                                       'minute': '00', 'operation_name': 'ABC', 'status': 'Start'}) == datetime(2022, 2, 1, 12, 0)


def test_get_timedelta():
    assert get_timedelta(
        datetime(2022, 2, 1, 10, 0), datetime(2022, 2, 1, 12, 0)) == timedelta(hours=2)
