from typing import Callable, Any
from time import time
from functools import wraps
from logging import getLogger, Logger, INFO
from sys import __stdout__
from datetime import datetime

def get_execution_time_log(pretty: bool = True, log_level: int = INFO, logger: Logger = None):
    """Simple method to output to logger the execution time for a method. The method will
    output in a reasonable unit of measure

    Args:
        func (Callable): function to be evaluated the time of
    """

    if not isinstance(pretty, bool):
        raise TypeError("pretty must be a boolean")

    if not isinstance(log_level, int):
        raise TypeError("log_level must be an integer")
    elif log_level < 0:
        raise ValueError("log_level must be greater than 0")

    if logger:
        if not isinstance(logger, Logger):
            raise TypeError("logger must be a logging.Logger instance")
    else:
        logger = getLogger("execution-time")

    def decorator(func: Callable):

        @wraps(func)
        def get_execution_time(*args, **kwargs):
            start = time() if pretty else datetime.now()
            result: Any = func(*args, **kwargs)  # save the result to a name
            compute_time = (time() if pretty else datetime.now()) - start
            if pretty:
                if compute_time < 0.1:
                    logger.log(
                        log_level,
                        "Computation time for %s: %.2f ms"
                        % (func.__name__, compute_time * 1000)
                    )
                elif compute_time < 60:
                    logger.log(
                        log_level,
                        "Computation time for %s: %.2f s" % (func.__name__, compute_time)
                    )
                elif compute_time / 60 < 60:
                    logger.log(
                        log_level,
                        "Computation time for %s: %.1f min"
                        % (func.__name__, (compute_time) / 60)
                    )
                else:
                    logger.log(
                        log_level,
                        "Computation time for %s: %.1f h"
                        % (func.__name__, (compute_time) / 3600)
                    )
            else:
                logger.log(
                    log_level,
                    "Computation time for %s: %s"
                    % (func.__name__, str(compute_time))
                )
            return result  # return the name

        return get_execution_time

    return decorator
