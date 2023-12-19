"""
This module is responsible for running functions with a timeout.

We use the decorator from decorator.py to implement this functionality
in the timeout_fn function.
"""

from .decorator import timeout


def timeout_fn(seconds, func, params_list=[], params_dict={}, fallback=None):
    """
    Execute the given function with a timeout.

    Args:
        seconds (int): The timeout duration in seconds.
        func (callable): The function to be executed.
        params_list (list, optional): The positional arguments
            to be passed to the function.
        params_dict (dict, optional): The keyword arguments to
            be passed to the function.
        fallback (callable, optional): The fallback function
            to be executed if the timeout occurs.

    Returns:
        The result of the executed function.

    """
    params_list = params_list or []
    params_dict = params_dict or {}
    decorated_func = (
        timeout(seconds=seconds, fallback=fallback)(func)
        if fallback
        else timeout(seconds=seconds)(func)
    )
    return decorated_func(*params_list, **params_dict)
