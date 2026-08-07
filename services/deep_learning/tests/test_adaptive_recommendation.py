"""
Tests for adaptive recommendation engine.
"""

from __future__ import annotations

from dl.continuous_learning.recommendation.adaptive_recommendation_engine import (
    AdaptiveRecommendationEngine,
)
from dl.models.learning.solver_performance_profile import (
    SolverPerformanceProfile,
)


def test_solver_recommendation() -> None:
    """
    Best solver is recommended.
    """

    engine = AdaptiveRecommendationEngine()

    recommendation = engine.recommend(
        (
            SolverPerformanceProfile(
                solver_name="solver_a",
                total_runs=10,
                success_rate=0.80,
                average_accuracy=0.85,
                average_energy=-30.0,
                average_runtime=20.0,
            ),
            SolverPerformanceProfile(
                solver_name="solver_b",
                total_runs=10,
                success_rate=0.95,
                average_accuracy=0.92,
                average_energy=-35.0,
                average_runtime=15.0,
            ),
        ),
    )

    assert recommendation.recommended_solver == ("solver_b")

    assert recommendation.confidence == 0.95
