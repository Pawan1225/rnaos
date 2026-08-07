"""
RNAOS large scale benchmark analysis model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class LargeScaleAnalysis:
    """
    Immutable large benchmark analysis.
    """

    analysis_id: str

    total_experiments: int

    average_accuracy: float

    average_energy_gap: float

    average_runtime: float

    benchmark_version: str
