"""
RNAOS biological mathematics utilities.
"""

from __future__ import annotations


def safe_divide(
    numerator: float,
    denominator: float,
) -> float:
    """
    Safely divide two values.

    Returns 0.0 if the denominator is zero.
    """
    if denominator == 0:
        return 0.0

    return numerator / denominator
