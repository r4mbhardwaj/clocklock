"""Provides a decorator for function timeout."""


from functools import wraps
import inspect
import threading


class TimeoutException(Exception):
    """Exception raised when a timeout occurs."""


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

    class TimeoutThread(threading.Thread):
        def __init__(self, function, args, kwargs):
            super().__init__()
            self.function = function
            self.args = args
            self.kwargs = kwargs
            self.result = None
            self.exception = None
            self.event = threading.Event()

        def run(self):
            try:
                self.result = self.function(*self.args, **self.kwargs)
            except Exception as exc:
                self.exception = exc
            self.event.set()

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            timeout_thread = TimeoutThread(func, args, kwargs)
            timeout_thread.start()
            timeout_thread.event.wait(timeout=seconds)

            if not timeout_thread.event.is_set():
                # The function did not finish before the timeout
                if inspect.signature(fallback).parameters:
                    return fallback(*args, **kwargs)
                else:
                    return fallback()

            if timeout_thread.exception:
                raise timeout_thread.exception

            return timeout_thread.result

        return wrapper

    return decorator
