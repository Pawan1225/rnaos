"""
RNAOS energy gap analysis model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class EnergyGapAnalysis:
    """
    Immutable energy gap analysis result.
    """

    analysis_id: str

    sample_count: int

    average_gap: float

    minimum_gap: float

    maximum_gap: float

    stability_score: float

    benchmark_version: str
