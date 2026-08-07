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
    Immutable statistical benchmark summary.
    """

    metric_name: str

    sample_count: int

    mean: float

    minimum: float

    maximum: float

    standard_deviation: float

    stability_score: float

    version: str
