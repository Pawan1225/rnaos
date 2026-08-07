"""
RNAOS adaptive recommendation engine.
"""

from __future__ import annotations

from dl.models.learning.adaptive_recommendation import (
    AdaptiveRecommendation,
)
from dl.models.learning.solver_performance_profile import (
    SolverPerformanceProfile,
)


class AdaptiveRecommendationEngine:
    """
    Generates optimization recommendations.
    """

    def recommend(
        self,
        profiles: tuple[
            SolverPerformanceProfile,
            ...,
        ],
    ) -> AdaptiveRecommendation:
        """
        Select best historical solver.
        """

        if not profiles:
            return AdaptiveRecommendation(
                recommended_solver="",
                optimization_strategy="",
                expected_accuracy=0.0,
                expected_runtime=0.0,
                confidence=0.0,
                reasoning=("No historical data",),
            )

        best = max(
            profiles,
            key=lambda profile: profile.success_rate,
        )

        return AdaptiveRecommendation(
            recommended_solver=best.solver_name,
            optimization_strategy="hybrid",
            expected_accuracy=(best.average_accuracy),
            expected_runtime=(best.average_runtime),
            confidence=(best.success_rate),
            reasoning=("Selected from historical solver performance",),
        )
