"""
RNAOS benchmark summary model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class BenchmarkSummary:
    """
    Immutable benchmark summary.
    """

    benchmark_id: str

    total_experiments: int

    average_energy_gap: float

    average_accuracy: float

    average_runtime: float

    best_score: float

    version: str
