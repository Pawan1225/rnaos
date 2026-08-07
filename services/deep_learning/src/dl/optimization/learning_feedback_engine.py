"""
RNAOS learning feedback engine.
"""

from __future__ import annotations

from dl.models.optimization.learning_feedback import (
    LearningFeedback,
)


class LearningFeedbackEngine:
    """
    Generates solver learning feedback.
    """

    def generate(
        self,
        solver_name: str,
        fitness: float,
        execution_time: float,
    ) -> LearningFeedback:
        """
        Generate feedback signal.
        """

        if execution_time <= 0:
            raise ValueError(
                "Execution time must be positive",
            )

        quality_score = max(
            0.0,
            min(
                1.0,
                fitness,
            ),
        )

        efficiency_score = 1.0 / (1.0 + execution_time)

        reward = quality_score * efficiency_score

        return LearningFeedback(
            solver_name=solver_name,
            reward=reward,
            quality_score=quality_score,
            efficiency_score=efficiency_score,
        )
