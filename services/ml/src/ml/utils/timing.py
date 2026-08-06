from __future__ import annotations

import time


def now() -> float:
    """
    High-resolution timer.
    """
    return time.perf_counter()
