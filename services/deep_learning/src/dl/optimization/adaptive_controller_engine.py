"""
RNAOS adaptive optimization controller.
"""

from __future__ import annotations

from dl.models.optimization.controller_decision import (
    ControllerDecision,
)
from dl.models.optimization.solver_recommendation import (
    SolverRecommendation,
)


class AdaptiveControllerEngine:
    """
    Converts solver recommendations into controller decisions.
    """

    def decide(
        self,
        problem_type: str,
        recommendation: SolverRecommendation,
    ) -> ControllerDecision:
        """
        Create an adaptive optimization decision.
        """

        if not problem_type:
            raise ValueError(
                "Problem type cannot be empty",
            )

        if not recommendation.solver:
            raise ValueError(
                "Recommended solver cannot be empty",
            )

        if not 0.0 <= recommendation.confidence <= 1.0:
            raise ValueError(
                "Confidence must be between 0 and 1",
            )

        return ControllerDecision(
            problem_type=problem_type,
            selected_solver=recommendation.solver,
            confidence=recommendation.confidence,
            learned=True,
        )
