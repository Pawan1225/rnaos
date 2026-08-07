"""
RNAOS learning profile engine.
"""

from __future__ import annotations

from dl.models.optimization.learning_feedback import (
    LearningFeedback,
)
from dl.models.optimization.learning_profile import (
    LearningProfile,
)


class LearningProfileEngine:
    """
    Generates learning intelligence profiles.
    """

    def generate(
        self,
        feedbacks: tuple[LearningFeedback, ...],
    ) -> LearningProfile:
        """
        Generate a learning intelligence profile.
        """

        if not feedbacks:
            raise ValueError(
                "Feedback history cannot be empty",
            )

        best = max(
            feedbacks,
            key=lambda feedback: feedback.reward,
        )

        average_reward = sum(feedback.reward for feedback in feedbacks) / len(feedbacks)

        confidence = max(
            0.0,
            min(
                1.0,
                average_reward,
            ),
        )

        return LearningProfile(
            total_experiences=len(
                feedbacks,
            ),
            best_solver=best.solver_name,
            average_reward=average_reward,
            confidence=confidence,
        )
