# ClockLock

A streamlined Python utility that gracefully enforces timeouts on your Python functions. Crafted with precision and simplicity, ClockLock lets you leash your function time execution with ease. With its featured decorator and function runner, both equipped with a fallback mechanism, maintaining a smooth control flow has never been more efficient.

## How It Works
ClockLock uses Python's concurrency mechanisms to keep your functions punctual. Providing an easy-to-use decorator and a direct function runner, your functions can be executed with a specified timeout limit - all within a few lines of code. If a function exceeds its time, a fallback function is triggered, facilitating a smooth control flow. Easy to set up and handy in its use, ClockLock guarantees your Python functions never overstay their welcome.

## Why ClockLock?
- **Graceful**: ClockLock manages function timeout smoothly and efficiently.
- **Fallback mechanism**: Provides an option to execute a fallback function if the primary function exceeds the given time.
- **Versatile**: Equally suited for small scripts and large applications.
- **Pythonic**: A clean, minimal, and familiar Python interface.

## Features
- **Decorator**: Simply annotate a function with `@clocklock.timeout(seconds=10)` to keep it in check.
- **Function runner**: Use `clocklock.timeout_fn(run_fn, timeout, fallback_fn, args, kwargs)` to control the execution of a function.
- **Fallback function**: Define a fallback function which gets triggered in case the primary function timeouts.

## Installation

Use pip to install:

```bash
pip install clocklock
```

Or, if you use Poetry:

```bash
poetry add clocklock
```

## Usage
First, import ClockLock:

```python
from clocklock import timeout, timeout_fn
```

Then, you can register a function for timeout:

```python
@timeout(seconds=1, fallback=lambda:"Fallback Task Complete")
def slow_function():
    time.sleep(2)
    return "done"

slow_function() # returns "Fallback Task Complete"
```
Or, use the function runner:
```python
def slow_function():
    time.sleep(2)
    return "done"

def fallback_func():
    print("Primary function exceeded time limit.")
timeout_fn(seconds=1, func=slow_function, fallback=fallback_func) # prints "Primary function exceeded time limit."
```

Please view the 'examples' directory for detailed usage examples.

## Contributing
We encourage you to contribute to ClockLock! Please check out the [Contributing to ClockLock guide](CONTRIBUTING.md) for guidelines about how to proceed.

## License
ClockLock is released under the [MIT License](LICENSE.md).
