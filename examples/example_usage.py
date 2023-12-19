from clocklock import timeout_fn
import time


def long_running_task():
    time.sleep(5)  # This task takes 5 seconds to finish
    return "Task Complete!"


def fallback_task():
    return "Fallback Task Complete!"


# Run the task with a timeout of 3 seconds.
# long_running_task should timeout and thus fallback_task will be executed.
result = timeout_fn(seconds=3, func=long_running_task, fallback=fallback_task)
print(result)  # This will print "Fallback Task Complete!"

# If we set timeout greater than time taken by
# long_running_task, it should not timeout.
result = timeout_fn(seconds=10, func=long_running_task, fallback=fallback_task)
print(result)  # This will print "Task Complete!"
