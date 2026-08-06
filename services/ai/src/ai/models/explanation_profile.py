"""
RNAOS explainable AI profile model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class ExplanationProfile:
    """
    Immutable explainable AI profile.

    Provides human-readable reasoning for AI-generated
    optimization recommendations.
    """

    recommended_strategy: str

    confidence: float

    biological_factors: tuple[str, ...]

    ai_factors: tuple[str, ...]

    recommendation_summary: str

    technical_summary: str

    @property
    def factor_count(
        self,
    ) -> int:
        """
        Total number of explanation factors.
        """
        return len(self.biological_factors) + len(self.ai_factors)
