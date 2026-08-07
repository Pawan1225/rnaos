"""
RNAOS adaptive optimization profile engine.
"""

from __future__ import annotations

from dl.models.optimization.adaptive_optimization_profile import (
    AdaptiveOptimizationProfile,
)
from dl.models.optimization.intelligence_score import (
    IntelligenceScore,
)
from dl.models.optimization.learning_profile import (
    LearningProfile,
)
from dl.models.optimization.meta_intelligence_profile import (
    MetaIntelligenceProfile,
)


class AdaptiveOptimizationProfileEngine:
    """
    Generates adaptive optimization profiles.
    """

    def generate(
        self,
        intelligence_score: IntelligenceScore,
        learning_profile: LearningProfile,
        meta_profile: MetaIntelligenceProfile,
    ) -> AdaptiveOptimizationProfile:
        """
        Generate adaptive optimization profile.
        """

        adaptability = (
            intelligence_score.overall_score + learning_profile.confidence + meta_profile.confidence
        ) / 3.0

        return AdaptiveOptimizationProfile(
            best_solver=learning_profile.best_solver,
            intelligence_score=(intelligence_score.overall_score),
            learning_confidence=(learning_profile.confidence),
            meta_confidence=(meta_profile.confidence),
            adaptability=adaptability,
        )
