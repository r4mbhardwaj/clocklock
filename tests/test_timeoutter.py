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


import threading
import time
from clocklock import timeout_fn


def run_with_timeout_and_collect(results, id, seconds=1, fallback=None):
    def long_running_function():
        time.sleep(seconds - 0.5)  # Making sure it completes before the timeout
        return f"Function completed successfully: {id}"

    result = timeout_fn(
        seconds=seconds,
        func=long_running_function,
        fallback=fallback,
    )
    results[id] = result


def test_run_with_timeout_in_threads():
    number_of_threads = 10
    timeout_duration = 1
    results = {}

    # Start all threads
    threads = []
    for i in range(number_of_threads):
        thread = threading.Thread(
            target=run_with_timeout_and_collect, args=(results, i, timeout_duration)
        )
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Check the results
    for i in range(number_of_threads):
        assert (
            results[i] == f"Function completed successfully: {i}"
        ), f"Test failed for thread {i}"
