"""
Integration tests for adaptive optimization controller.
"""

from __future__ import annotations

from dl.models.optimization.controller_decision import (
    ControllerDecision,
)
from dl.models.optimization.learning_feedback import (
    LearningFeedback,
)
from dl.optimization.adaptive_controller_engine import (
    AdaptiveControllerEngine,
)
from dl.optimization.solver_recommendation_learner import (
    SolverRecommendationLearner,
)


def test_complete_learning_loop() -> None:
    """
    Feedback drives solver selection.
    """

    feedback_history = (
        LearningFeedback(
            solver_name="genetic",
            reward=0.70,
            quality_score=0.80,
            efficiency_score=0.90,
        ),
        LearningFeedback(
            solver_name="differential_evolution",
            reward=0.92,
            quality_score=0.95,
            efficiency_score=0.97,
        ),
        LearningFeedback(
            solver_name="pso",
            reward=0.75,
            quality_score=0.85,
            efficiency_score=0.88,
        ),
    )

    learner = SolverRecommendationLearner()

    recommendation = learner.recommend(
        problem_type="rna_optimization",
        feedbacks=feedback_history,
    )

    controller = AdaptiveControllerEngine()

    decision = controller.decide(
        problem_type="rna_optimization",
        recommendation=recommendation,
    )

    assert isinstance(
        decision,
        ControllerDecision,
    )

    assert decision.selected_solver == "differential_evolution"

    assert decision.learned is True

    assert decision.confidence == 0.92
