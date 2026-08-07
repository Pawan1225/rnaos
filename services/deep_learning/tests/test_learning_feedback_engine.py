"""
Tests for learning feedback engine.
"""

from __future__ import annotations

from dl.models.optimization.learning_feedback import (
    LearningFeedback,
)
from dl.optimization.learning_feedback_engine import (
    LearningFeedbackEngine,
)


def test_learning_feedback_generation() -> None:
    """
    Feedback signal is generated.
    """

    engine = LearningFeedbackEngine()

    feedback = engine.generate(
        solver_name="genetic",
        fitness=0.9,
        execution_time=1.0,
    )

    assert isinstance(
        feedback,
        LearningFeedback,
    )

    assert feedback.solver_name == "genetic"

    assert feedback.quality_score == 0.9

    assert feedback.efficiency_score == 0.5

    assert feedback.reward == 0.45
