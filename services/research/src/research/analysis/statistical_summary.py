"""
Statistical summary model for RNAOS research experiments.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class StatisticalSummary:
    """
    Aggregate statistics computed from a collection of experiment metrics.
    """

    sample_size: int

    mean_runtime: float
    median_runtime: float
    std_runtime: float

    fastest_runtime: float
    slowest_runtime: float

    mean_absolute_error: float
    median_absolute_error: float
    std_absolute_error: float

    mean_relative_error: float

    mean_accuracy: float

    @property
    def has_samples(self) -> bool:
        """Return True when the summary contains experiment results."""
        return self.sample_size > 0
