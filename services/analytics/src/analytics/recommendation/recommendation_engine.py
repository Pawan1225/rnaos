"""
Recommendation analytics.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum

from analytics.performance import SolverPerformance

CONFIDENCE_WEIGHT = 100.0
RUNTIME_WEIGHT = 10.0
EXPERIENCE_WEIGHT = 1.0


class RecommendationLevel(StrEnum):
    """Recommendation category."""

    RECOMMENDED = "RECOMMENDED"
    MONITOR = "MONITOR"
    AVOID = "AVOID"


@dataclass(slots=True)
class SolverRecommendation:
    """Recommendation for solver selection."""

    recommended_solver: str
    confidence: float
    level: RecommendationLevel
    score: float
    reason: str
    alternatives: list[str]


class RecommendationEngine:
    """Recommend solvers using historical analytics."""

    def recommend(
        self,
        performance: list[SolverPerformance],
    ) -> SolverRecommendation:
        """Recommend the best solver."""

        if not performance:
            raise ValueError("No performance data available.")

        scored: list[tuple[float, SolverPerformance]] = []

        for solver in performance:
            score = (
                CONFIDENCE_WEIGHT * solver.mean_confidence
                - RUNTIME_WEIGHT * solver.mean_runtime
                + EXPERIENCE_WEIGHT * solver.experiments
            )

            scored.append((score, solver))

        scored.sort(
            key=lambda item: (
                item[0],
                item[1].solver,
            ),
            reverse=True,
        )

        best_score, best_solver = scored[0]

        return SolverRecommendation(
            recommended_solver=best_solver.solver,
            confidence=best_solver.mean_confidence,
            level=RecommendationLevel.RECOMMENDED,
            score=best_score,
            reason=(
                "Highest historical confidence with competitive runtime "
                "and the strongest supporting evidence."
            ),
            alternatives=[solver.solver for _, solver in scored[1:]],
        )
