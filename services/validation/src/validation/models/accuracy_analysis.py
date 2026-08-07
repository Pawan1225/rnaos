"""
RNAOS accuracy analysis model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class AccuracyAnalysis:
    """
    Immutable accuracy analysis result.
    """

    analysis_id: str

    sample_count: int

    average_accuracy: float

    minimum_accuracy: float

    maximum_accuracy: float

    benchmark_version: str
