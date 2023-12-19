"""Provides a decorator for function timeout."""


import signal
from functools import wraps
import inspect


class TimeoutException(Exception):
    """Exception raised when a timeout occurs."""


def _timeout_handler(signum, frame):
    """
    Timeout handler function that raises a TimeoutException.

    Args:
        signum (int): The signal number.
        frame (frame): The current stack frame.

    Raises:
        TimeoutException: Exception indicating a timeout occurred.
    """
    raise TimeoutException()


def timeout(seconds=1, fallback=lambda: "Function timed out!"):
    """
    Add a timeout to a function.

    Args:
        seconds (int): The number of seconds before the function times
            out. Default is 1 second.
        fallback (function): The fallback function to be called if the
            function times out. Default is a lambda function that
            returns "Function timed out!".

    Returns:
        function: The decorated function with the timeout functionality.
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _timeout_handler)
            signal.alarm(seconds)
            try:
                result = func(*args, **kwargs)
            except TimeoutException:
                # Check if fallback needs arguments
                if inspect.signature(fallback).parameters:
                    result = fallback(*args, **kwargs)
                else:
                    result = fallback()
            finally:
                signal.alarm(0)
            return result

        return wrapper

    return decorator
