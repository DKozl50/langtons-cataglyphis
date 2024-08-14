import time

from collections.abc import Callable
from typing import TypeAlias, TypeVar


RT = TypeVar("RT")
TimeType: TypeAlias = float


def measure_manual(func: Callable[..., None]) -> TimeType:
    """Used to measure `evaluate` function, which does not return anything."""
    time_start = time.monotonic()

    func()

    time_end = time.monotonic()
    return time_end - time_start
