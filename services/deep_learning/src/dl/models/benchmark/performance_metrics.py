"""
RNAOS performance evaluation metrics model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class PerformanceMetrics:
    """
    Immutable computational performance metrics.
    """

    runtime: float

    memory_usage: float

    cpu_usage: float

    iterations: int

    solver_calls: int

    scalability_score: float
