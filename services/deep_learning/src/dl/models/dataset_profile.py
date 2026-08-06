"""
RNAOS dataset intelligence profile model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class DatasetProfile:
    """
    Immutable dataset intelligence profile.
    """

    dataset_name: str

    sample_count: int

    feature_dimension: int

    readiness_score: float
