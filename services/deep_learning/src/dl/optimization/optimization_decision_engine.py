"""
RNAOS optimization decision engine.
"""

from __future__ import annotations

from dl.models.optimization.optimization_decision import (
    OptimizationDecision,
)


class OptimizationDecisionEngine:
    """
    Generates optimization decisions.
    """

    def decide(
        self,
        sequence_length: int,
        complexity: float,
        folding_difficulty: float,
    ) -> OptimizationDecision:
        """
        Decide optimization strategy.
        """

        if sequence_length > 500:
            return OptimizationDecision(
                strategy="tensor",
                confidence=0.85,
                reasoning=("Large RNA sequences require compressed search spaces."),
            )

        if complexity > 0.75:
            return OptimizationDecision(
                strategy="annealing",
                confidence=0.80,
                reasoning=("Complex energy landscapes benefit from exploration."),
            )

        if folding_difficulty > 0.7:
            return OptimizationDecision(
                strategy="hybrid",
                confidence=0.85,
                reasoning=("Difficult folding problems benefit from multiple solvers."),
            )

        return OptimizationDecision(
            strategy="qubo",
            confidence=0.75,
            reasoning=("Structured problems benefit from mathematical formulation."),
        )
