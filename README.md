# Execution Time Wrapper

A simple package with a few method to get the execution time of methods through wrapping.

## Usage

Currently, the package contains two methods, one which returns to sdout (print) and one which goes to a logger.

```python
from execution_time import get_execution_time_log

@get_execution_time_log
def my_fun():
    print("Hello World!")
```
The same for the other method given, i.e. `get_execution_time_print`.

## TODOs

[ ] Implement logger level

@2022, Leonardo Alchieri

<sub>People-Centered Computing Lab - [Università della Svizzera italiana, Switzerland](https://www.usi.ch/en)</sub>
