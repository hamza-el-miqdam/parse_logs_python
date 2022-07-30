from src.log_parser.log_parser import parse_log_lines, get_operations_run_time_from_logs_lines, get_operations_avg_time_from_logs_lines, from_string, get_operations_avg_time_from_run_time, from_file
from datetime import timedelta, timedelta

logs_1 = "2022-02-01T10:00 Operation ABC Start"
logs_2 = "2022-02-01T10:00 Operation ABC Start\n2022-02-01T12:00 Operation ABC End"


logs_lines_1 = [
    {
        'year': '2022',
        'month': '02',
        'day': '01',
        'hour': '10',
        'minute': '00',
        'operation_name': 'ABC',
        'status': 'Start'
    }
]

logs_lines_2 = [
    {
        'year': '2022',
        'month': '02',
        'day': '01',
        'hour': '10',
        'minute': '00',
        'operation_name': 'ABC',
        'status': 'Start'
    },
    {
        'year': '2022',
        'month': '02',
        'day': '01',
        'hour': '12',
        'minute': '00',
        'operation_name': 'ABC',
        'status': 'End'
    }
]

logs_lines_3 = [
    {
        'year': '2022',
        'month': '02',
        'day': '01',
        'hour': '10',
        'minute': '00',
        'operation_name': 'ABC',
        'status': 'Start'},
    {
        'year': '2022',
        'month': '02',
        'day': '01',
        'hour': '12',
        'minute': '00',
        'operation_name': 'ABC',
        'status': 'End'
    },
    {
        'year': '2022',
        'month': '02',
        'day': '01',
        'hour': '12',
        'minute': '02',
        'operation_name': 'DEF',
        'status': 'Start'
    },
    {
        'year': '2022',
        'month': '02',
        'day': '01',
        'hour': '13',
        'minute': '02',
        'operation_name': 'DEF',
        'status': 'End'
    }
]

logs_lines_4 = [
    {
        'year': '2022',
        'month': '02',
        'day': '01',
        'hour': '10',
        'minute': '00',
        'operation_name': 'ABC',
        'status': 'Start'},
    {
        'year': '2022',
        'month': '02',
        'day': '01',
        'hour': '13',
        'minute': '00',
        'operation_name': 'ABC',
        'status': 'End'
    },
    {
        'year': '2022',
        'month': '02',
        'day': '01',
        'hour': '13',
        'minute': '02',
        'operation_name': 'ABC',
        'status': 'Start'
    },
    {
        'year': '2022',
        'month': '02',
        'day': '01',
        'hour': '18',
        'minute': '02',
        'operation_name': 'ABC',
        'status': 'End'
    },
    {
        'year': '2022',
        'month': '02',
        'day': '01',
        'hour': '18',
        'minute': '03',
        'operation_name': 'ABC',
        'status': 'Start'
    },
    {
        'year': '2022',
        'month': '02',
        'day': '01',
        'hour': '20',
        'minute': '03',
        'operation_name': 'ABC',
        'status': 'End'
    }
]


def test_parse_log_lines_One_lines():
    assert parse_log_lines(logs_1) == logs_lines_1


def test_parse_log_lines_multi_lines():
    assert parse_log_lines(logs_2) == logs_lines_2


def test_get_operations_run_time_from_logs_lines_2_operations_1_runs():
    assert get_operations_run_time_from_logs_lines(logs_lines_2) == {
        "ABC": [timedelta(hours=2)]}


def test_2_get_operations_run_time_from_logs_lines_3_operations_1_runs_each():
    assert get_operations_run_time_from_logs_lines(logs_lines_3) == {
        "ABC": [timedelta(hours=2)],
        "DEF": [timedelta(hours=1)]
    }


def test_get_operations_run_time_from_logs_lines_2_operations_3_runs():
    assert get_operations_run_time_from_logs_lines(logs_lines_4) == {
        "ABC": [timedelta(hours=3), timedelta(hours=5), timedelta(hours=2)]
    }


def test_get_operations_avg_time_from_logs_lines_3_operations_1_runs_each():
    assert get_operations_avg_time_from_logs_lines(logs_lines_3) == {
        "ABC": timedelta(hours=2),
        "DEF": timedelta(hours=1)
    }


def test_2_get_operations_avg_time_from_logs_lines_2_operations_3_runs():
    assert get_operations_avg_time_from_logs_lines(logs_lines_4) == {
        "ABC": timedelta(hours=3, minutes=20)
    }


def test_get_operations_avg_time_1_operations_2_runs():
    assert get_operations_avg_time_from_run_time(
        {"ABC": [timedelta(hours=1), timedelta(hours=2)]}) == {"ABC": timedelta(hours=1, minutes=30)}


def test_2_get_operations_avg_time_2_operations_2_runs_and_3_runs():
    assert get_operations_avg_time_from_run_time(
        {"ABC": [timedelta(hours=1), timedelta(hours=2)], "DEF": [timedelta(hours=3), timedelta(hours=5), timedelta(hours=2)]}) == {"ABC": timedelta(hours=1, minutes=30), 'DEF': timedelta(hours=3, minutes=20)}


def test_log_parser():
    assert from_string(logs_2) == {
        "ABC": timedelta(hours=2)
    }

def test_input_from_file():
    assert from_file("./tests/test_input.txt") == {
        "ABC": timedelta(hours=3, minutes=20),
        "XYZ": timedelta(hours=10, minutes=2),
        "WXY": timedelta(minutes=3)
    }
