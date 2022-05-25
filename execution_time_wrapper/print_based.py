from typing import Callable, Any
from time import time
from functools import wraps
from sys import __stdout__

def get_execution_time_print(func: Callable):
    """Simple method to output to sdout the execution time for a method. The method will
    output in a reasonable unit of measure

    Args:
        func (Callable): function to be evaluated the time of
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result: Any = func(*args, **kwargs)  # save the result to a name
        compute_time: int = time() - start
        if compute_time < 0.1:
            print(
                "Computation time for %s: %.2f ms"
                % (func.__name__, compute_time * 1000)
            )
        elif compute_time < 60:
            print(
                "Computation time for %s: %.2f s" % (func.__name__, compute_time)
            )
        elif compute_time / 60 < 60:
            print(
                "Computation time for %s: %.1f min"
                % (func.__name__, (compute_time) / 60)
            )
        else:
            print(
                "Computation time for %s: %.1f h"
                % (func.__name__, (compute_time) / 3600)
            )
        return result  # return the name

    return wrapper