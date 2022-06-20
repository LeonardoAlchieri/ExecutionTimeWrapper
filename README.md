[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.org/project/execution-time-wrapper/)
[![PyPI version](https://badge.fury.io/py/execution-time-wrapper.svg)](https://badge.fury.io/py/execution-time-wrapper)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/pybadges.svg)](https://pypi.org/project/execution-time-wrapper/)
[![Downloads](https://pepy.tech/badge/execution-time-wrapper)](https://pepy.tech/project/execution-time-wrapper)

# Execution Time Wrapper

A simple package with a few method to get the execution time of methods through wrapping.

## Usage

Currently, the package contains two methods, one which returns to sdout (print) and one which goes to a logger. The method prints the time in a nice way, i.e. milliseconds, seconds, minutes or hours. For example:

```python
from execution_time_wrapper import get_execution_time_print, get_execution_time_log

@get_execution_time_print
def my_fun():
    print("Hello World!")
```
```python
my_fun()
```
```console
>> Hello World!
>> Computation time for my_fun: 0.02 ms
```
However, if the function takes more time:
```python
from execution_time_wrapper import get_execution_time_print, get_execution_time_log
from time import sleep

@get_execution_time_print
def my_fun():
    sleep(4)
    print("Hello World!")
```
```python
my_fun()
```
```console
>> Hello World!
>> Computation time for my_fun: 4.00 s
```

The same for the other method given, i.e. `get_execution_time_log`.

## TODOs

[ ] Implement logger level

@2022, Leonardo Alchieri

<sub>People-Centered Computing Lab - [Università della Svizzera italiana, Switzerland](https://www.usi.ch/en)</sub>
