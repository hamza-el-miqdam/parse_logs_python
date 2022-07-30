# Log parser

  ## Context

I created this project for an assignment given by Meero

The objective of this assignment is to read lines from a log file in this format:
```
2022-02-01T10:00 Operation ABC Start
2022-02-01T10:01 Operation ABC End
2022-02-01T10:02 Operation DEF Start
2022-02-01T10:08 Operation XYZ Start
2022-02-01T20:09 Operation WXY Start
2022-02-01T20:10 Operation XYZ End
2022-02-01T20:12 Operation WXY End
```
Parse the file and return average run time for every operation

## Examples of How To Use
the log parser accepts 2 types of inputs :
A file, where you can give it a file path :
```python
from log_parser import log_parser
average_time = log_parser.from_file('meero-test-python/tests/test_input.txt')
```
A well formatted string :
```python
from log_parser import log_parser
average_time = log_parser.from_string("2022-02-01T10:00 Operation ABC Start\n2022-02-01T12:00 Operation ABC End")
```
A print function is included in the package, you can use it like so :
```python
from log_parser import log_parser
average_time = log_parser.from_file('meero-test-python/tests/test_input.txt')

log_parser.print_operations_avg_time(average_time)
```
You will have something like that in the console:

```
The operation named ABC spend in average 3:20:00
The operation named XYZ spend in average 10:02:00
The operation named WXY spend in average 0:03:00
```

## Output
The package give a simple dictionary as output, the keys of the dictionary are the operations names and the value is a time delta 
Example
```
{
	'ABC': datetime.timedelta(seconds=12000), 
	'XYZ': datetime.timedelta(seconds=36120), 
	'WXY': datetime.timedelta(seconds=180)
}
```
