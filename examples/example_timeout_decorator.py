from clocklock import timeout
import time


@timeout(seconds=3, fallback=lambda: "Fallback Task Complete!")
def long_running_task():
    time.sleep(5)  # This task takes 5 seconds to finish
    return "Task Complete!"


# Run the decorated task. It should timeout
# and thus the fallback function will be called.
result = long_running_task()
print(result)  # This will print "Fallback Task Complete!"
