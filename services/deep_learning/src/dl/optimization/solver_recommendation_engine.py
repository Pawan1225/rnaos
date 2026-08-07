"""
RNAOS solver recommendation engine.
"""

from __future__ import annotations

from dl.models.optimization.solver_recommendation import (
    SolverRecommendation,
)


class SolverRecommendationEngine:
    """
    Recommends optimization strategies.
    """

    def recommend(
        self,
        sequence_length: int,
        complexity: float,
        constraint_density: float,
    ) -> SolverRecommendation:
        """
        Select best optimization strategy.
        """

        if sequence_length > 500:
            return SolverRecommendation(
                solver="tensor",
                confidence=0.85,
                reasoning=("Large sequences benefit from tensor compression."),
            )

        if complexity > 0.7:
            return SolverRecommendation(
                solver="annealing",
                confidence=0.80,
                reasoning=("Complex landscapes benefit from exploration."),
            )

        if constraint_density > 0.5:
            return SolverRecommendation(
                solver="qubo",
                confidence=0.75,
                reasoning=("Constraint-heavy problems benefit from QUBO formulation."),
            )

        return SolverRecommendation(
            solver="hybrid",
            confidence=0.70,
            reasoning=("Multiple methods provide balanced optimization."),
        )
