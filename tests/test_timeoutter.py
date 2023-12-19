import time
from clocklock import timeout_fn


def test_run_with_timeout():
    def long_running_function():
        time.sleep(2)
        return "Function completed successfully"

    result = timeout_fn(seconds=1, func=long_running_function)
    assert result == "Function timed out!"


def test_run_with_timeout_with_fallback():
    def long_running_function():
        time.sleep(2)
        return "Function completed successfully"

    result = timeout_fn(
        seconds=1,
        func=long_running_function,
        fallback=lambda: "Fallback function called",
    )
    assert result == "Fallback function called"
