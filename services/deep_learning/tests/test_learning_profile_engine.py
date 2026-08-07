"""
Tests for learning profile engine.
"""

from __future__ import annotations

from dl.models.optimization.learning_feedback import (
    LearningFeedback,
)
from dl.models.optimization.learning_profile import (
    LearningProfile,
)
from dl.optimization.learning_profile_engine import (
    LearningProfileEngine,
)


def test_learning_profile_generation() -> None:
    """
    Learning profile is generated.
    """

    engine = LearningProfileEngine()

    profile = engine.generate(
        (
            LearningFeedback(
                solver_name="genetic",
                reward=0.8,
                quality_score=0.9,
                efficiency_score=0.8,
            ),
            LearningFeedback(
                solver_name="pso",
                reward=0.95,
                quality_score=0.95,
                efficiency_score=1.0,
            ),
        )
    )

    assert isinstance(
        profile,
        LearningProfile,
    )

    assert profile.total_experiences == 2

    assert profile.best_solver == "pso"

    assert profile.confidence > 0
