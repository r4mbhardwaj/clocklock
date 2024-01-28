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


import threading
import queue


def test_with_threading():
    def run_long_running_function(results_queue):
        result = long_running_function()
        results_queue.put(result)

    @timeout(seconds=3, fallback=lambda: (False, ["Profanity timeout"]))
    def long_running_function():
        time.sleep(2)
        return "Function completed successfully"

    threads = []
    results_queue = queue.Queue()
    for _ in range(10):
        t = threading.Thread(target=run_long_running_function, args=(results_queue,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    results = []
    while not results_queue.empty():
        results.append(results_queue.get())

    print(results)
    assert all([result == "Function completed successfully" for result in results])
