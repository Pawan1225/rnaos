"""
RNAOS adaptive decision engine.
"""

from __future__ import annotations

from dl.models.optimization.decision_context import (
    DecisionContext,
)
from dl.models.optimization.solver_recommendation import (
    SolverRecommendation,
)
from dl.optimization.solver_intelligence_registry import (
    SolverIntelligenceRegistry,
)


class AdaptiveDecisionEngine:
    """
    Selects the optimal solver strategy.
    """

    def decide(
        self,
        context: DecisionContext,
        registry: SolverIntelligenceRegistry,
    ) -> SolverRecommendation:
        """
        Generate a solver recommendation.
        """

        # Context is reserved for future decision logic.
        _ = context

        best_solver = registry.best_solver()

        return SolverRecommendation(
            solver=best_solver.solver_name,
            confidence=best_solver.capability_score,
            reasoning="highest capability",
        )
