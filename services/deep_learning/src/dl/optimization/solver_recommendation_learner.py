"""
RNAOS solver recommendation learner.
"""

from __future__ import annotations

from dl.models.optimization.learning_feedback import (
    LearningFeedback,
)
from dl.models.optimization.solver_recommendation import (
    SolverRecommendation,
)


class SolverRecommendationLearner:
    """
    Learns the best solver from historical feedback.
    """

    def recommend(
        self,
        problem_type: str,
        feedbacks: tuple[LearningFeedback, ...],
    ) -> SolverRecommendation:
        """
        Recommend the highest-reward solver.
        """

        if not feedbacks:
            raise ValueError(
                "Feedback history cannot be empty",
            )

        best = max(
            feedbacks,
            key=lambda feedback: feedback.reward,
        )

        return SolverRecommendation(
            solver=best.solver_name,
            confidence=min(
                1.0,
                best.reward,
            ),
            reasoning=(
                f"Recommended for problem type "
                f"'{problem_type}' based on the "
                f"highest historical reward."
            ),
        )
