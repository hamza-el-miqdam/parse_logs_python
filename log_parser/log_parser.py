"""
This module parse logs and calculate the average run time of a set of operations
"""
import re
from datetime import datetime, timedelta


def parse_log_lines(logs):
    """
    Parse the informations from the logs using a regex.

    Parameters
    ----------

    logs : str
        the log line in string format.

    Returns
    -------

    log_lines : ( list of dict of year: str, month: str, day: str, hour: str, minute: str,
        operation_name: str, status: str )
        Informations from one line of log.
    """
    regex = r"^(?P<year>[0-9]*)-(?P<month>[0-9]*)-(?P<day>[0-9]*)T(?P<hour>[0-9]*):(?P<minute>[0-9]*) Operation (?P<operation_name>[A-Z]*) (?P<status>Start|End)$"
    logs_line_iterator = re.finditer(regex, logs, re.MULTILINE)
    
    log_lines = []
    for _, logs_line_match_object in enumerate(logs_line_iterator, start=1):
        log_lines.append(logs_line_match_object.groupdict())

    return log_lines


def get_datetime_from_log_line(log_line):
    """
    Calculate datetime form a given log line.

    Parameters
    ----------

    log_line : ( dict of year: str, month: str, day: str, hour: str, minute: str,
        operation_name: str, status: str )
        Informations from one line of log.

    Returns
    -------

    datetime : datetime
        The date and time of the logs line.
    """
    return datetime(int(log_line["year"]), int(log_line["month"]), int(
        log_line["day"]), int(log_line["hour"]), int(log_line["minute"]), 0)


def get_timedelta(start_datetime, end_datetime):
    """
    Calculate the run time of an operation.

    Parameters
    ----------

    start_datetime : datetime
        The date and time when the operation started.
    end_datetime : datetime
        The date and time when the operation ended.

    Returns
    -------

    timedelta : timedelta
        The run time of the operation.
    """
    return end_datetime - start_datetime


def get_operations_avg_time_from_run_time(operations_run_time):
    """
    Calculate the avarege run time of all operations.

    Parameters
    ----------

    operations_run_time : (dict of str: list of timedelta)
        all runs time of all operations.


    Returns
    -------

    operations_average_run_time : timedelta
        The average run time of all operations.
    """
    avg_run_time = {}
    for operation_name in operations_run_time:
    
        avg_run_time[operation_name] = sum(
            operations_run_time[operation_name], timedelta(0))/len(operations_run_time[operation_name])
    
    return avg_run_time


def get_operations_run_time_from_logs_lines(logs_lines):
    """
    Calculate all runs time of all operations.

    Parameters
    ----------

    log_lines : ( list of dict of year: str, month: str, day: str, hour: str, minute: str,
        operation_name: str, status: str )
        Informations from one line of log.

    Local Variables
    ---------------
    current_operations_start_time : ( dict of str: datetime)
        Store the start time of the current operations.
    current_operations_run_times: (dict of str: list of timedelta)
        Store all runs time of all operations.

    Returns
    -------

    operations_run_time : (dict of str: list of timedelta)
        all runs time of the operations.
    """
    current_operations_start_time = {}
    current_operations_run_times = {}

    for log_line in logs_lines:

        operation_name = log_line["operation_name"]
        status = log_line["status"]

        log_datetime = get_datetime_from_log_line(log_line)

        if status == 'Start':
            current_operations_start_time[operation_name] = log_datetime
        elif status == 'End' and operation_name in current_operations_start_time:
            operation_run_timedelta = get_timedelta(
                current_operations_start_time[operation_name], log_datetime)

            if not operation_name in current_operations_run_times:
                current_operations_run_times[operation_name] = []
            current_operations_run_times[operation_name].append(
                operation_run_timedelta)

            del current_operations_start_time[operation_name]
    return current_operations_run_times


def get_operations_avg_time_from_logs_lines(logs_lines):
    """
    Calculate the avarage run time of the operations

    Parameters
    ----------

    log_lines : ( list of dict of year: str, month: str, day: str, hour: str, minute: str,
        operation_name: str, status: str )
        Informations from one line of log.

    Returns
    -------

    average_operations_run_time : (dict of str: timedelta)
        The average operation run time of all operations.
    """

    operations_run_time = get_operations_run_time_from_logs_lines(logs_lines)

    return get_operations_avg_time_from_run_time(operations_run_time)


def print_operations_avg_time(average_operations_run_time):
    """
    Print in the console The average operation run time of all operations.

    Parameters
    ----------

    average_operations_run_time : (dict of str: timedelta)
        The average operation run time of all operations.

    """
    for operation_name in average_operations_run_time:
        avg_time = average_operations_run_time[operation_name]

        print("The operation named {operation_name} spend in average {avg_time}".format(
            operation_name=operation_name, avg_time=avg_time))


def parse_logs(logs):
    """
    Parse logs and extract for each operation the average run time

    Parameters
    ----------

    logs : str
        The logs in string format.

    Returns
    -------

    average_operations_run_time : (dict of str: timedelta)
        The average operation run time for each operations.

    """

    logs_lines = parse_log_lines(logs)

    average_operations_run_time = get_operations_avg_time_from_logs_lines(
        logs_lines)

    print_operations_avg_time(average_operations_run_time)

    return average_operations_run_time


def parse_logs_from_file(input_file_path):
    """
    Parse logs and extract for each operation the average run time

    Parameters
    ----------

    input_file_path : str
        The file where logs are stored.

    Returns
    -------

    average_operations_run_time : (dict of str: timedelta)
        The average operation run time for each operations.

    """
    file = open(input_file_path, "r")
    logs = file.read()

    return parse_logs(logs)

