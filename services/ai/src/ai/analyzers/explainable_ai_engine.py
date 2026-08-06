"""
RNAOS explainable AI engine.
"""

from __future__ import annotations

from ai.models.explanation_profile import (
    ExplanationProfile,
)
from ai.models.meta_feature_profile import (
    MetaFeatureProfile,
)
from ai.models.solver_recommendation_features import (
    SolverRecommendationFeatures,
)
from ai.utils.explanation_builder import (
    ai_factors,
    biological_factors,
    determine_strategy,
    recommendation_summary,
    technical_summary,
)
from biology.models.biological_intelligence_profile import (
    BiologicalIntelligenceProfile,
)


class ExplainableAIEngine:
    """
    Generate deterministic explanations for AI recommendations.

    Architecture
    ------------
    Converts biological intelligence, meta features,
    and solver recommendation features into
    human-readable explanations.

    Complexity
    ----------
    Time Complexity: O(1)
    """

    def analyze(
        self,
        profile: BiologicalIntelligenceProfile,
        meta_features: MetaFeatureProfile,
        recommendation: SolverRecommendationFeatures,
    ) -> ExplanationProfile:
        """
        Generate an explainable AI profile.
        """
        strategy = determine_strategy(
            recommendation,
        )

        bio = biological_factors(
            profile,
        )

        ai = ai_factors(
            meta_features,
        )

        summary = recommendation_summary(
            strategy,
        )

        technical = technical_summary(
            profile,
            meta_features,
            recommendation,
        )

        return ExplanationProfile(
            recommended_strategy=strategy,
            confidence=recommendation.recommendation_confidence,
            biological_factors=bio,
            ai_factors=ai,
            recommendation_summary=summary,
            technical_summary=technical,
        )
