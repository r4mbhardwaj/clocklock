"""
ClockLock: optimizing flow control with function timeouts.

This package includes a decorator and a function runner, each
with capabilities for fallback functionalities.
"""

from .decorator import timeout
from .timeoutter import timeout_fn


__all__ = ["timeout", "timeout_fn"]
