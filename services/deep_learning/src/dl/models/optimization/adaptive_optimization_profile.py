"""
RNAOS adaptive optimization profile model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class AdaptiveOptimizationProfile:
    """
    Immutable adaptive optimization profile.
    """

    best_solver: str

    intelligence_score: float

    learning_confidence: float

    meta_confidence: float

    adaptability: float
