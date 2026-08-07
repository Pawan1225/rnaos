"""
Tests for solver recommendation learner.
"""

from __future__ import annotations

from dl.models.optimization.learning_feedback import (
    LearningFeedback,
)
from dl.models.optimization.solver_recommendation import (
    SolverRecommendation,
)
from dl.optimization.solver_recommendation_learner import (
    SolverRecommendationLearner,
)


def test_solver_recommendation() -> None:
    """
    Highest reward solver is recommended.
    """

    learner = SolverRecommendationLearner()

    recommendation = learner.recommend(
        problem_type="rna_folding",
        feedbacks=(
            LearningFeedback(
                solver_name="genetic",
                reward=0.80,
                quality_score=0.90,
                efficiency_score=0.80,
            ),
            LearningFeedback(
                solver_name="pso",
                reward=0.95,
                quality_score=0.95,
                efficiency_score=1.00,
            ),
        ),
    )

    assert isinstance(
        recommendation,
        SolverRecommendation,
    )

    assert recommendation.solver == "pso"

    assert recommendation.confidence == 0.95

    assert "rna_folding" in recommendation.reasoning
