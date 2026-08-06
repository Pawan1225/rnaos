"""
RNAOS meta feature profile model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class MetaFeatureProfile:
    """
    Immutable higher-order AI features derived from
    biological intelligence.

    These composite features summarize biological,
    structural, and thermodynamic characteristics into
    AI-ready intelligence for downstream optimization
    and solver recommendation.
    """

    folding_difficulty: float

    structural_complexity: float

    optimization_complexity: float

    stability_complexity_index: float

    quantum_suitability: float

    ai_readiness_score: float

    @property
    def feature_count(
        self,
    ) -> int:
        """
        Number of meta features.
        """
        return 6
