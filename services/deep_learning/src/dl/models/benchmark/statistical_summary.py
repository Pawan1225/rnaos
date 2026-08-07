"""
RNAOS statistical summary model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class StatisticalSummary:
    """
    Immutable statistical summary.
    """

    mean: float

    median: float

    standard_deviation: float

    variance: float

    minimum: float

    maximum: float

    sample_size: int
