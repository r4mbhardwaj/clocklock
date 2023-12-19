import time
from clocklock import timeout


def test_timeout_decorator():
    @timeout(seconds=1)
    def long_running_function():
        time.sleep(2)
        return "Function completed successfully"

    result = long_running_function()
    assert result == "Function timed out!"


def test_timeout_decorator_with_fallback():
    @timeout(seconds=1, fallback=lambda: "Fallback function called")
    def long_running_function():
        time.sleep(2)
        return "Function completed successfully"

    result = long_running_function()
    assert result == "Fallback function called"


def test_timeout_decorator_with_fallback_with_args():
    statement = "Fallback function called with {}"

    @timeout(
        seconds=1,
        fallback=lambda *args, **kwargs: statement.format(kwargs.get("x")),
    )
    def long_running_function(x=None):
        time.sleep(2)
        return "Function completed successfully"

    term = 12
    result = long_running_function(x=term)
    assert result == statement.format(term)
