"""
RNAOS optimization intelligence evaluation engine.
"""

from __future__ import annotations

from dl.models.optimization.optimization_intelligence_evaluation import (
    OptimizationIntelligenceEvaluation,
)


class OptimizationIntelligenceEvaluationEngine:
    """
    Evaluates the optimization intelligence stack.
    """

    def evaluate(
        self,
        optimization_score: float,
        learning_score: float,
        evolution_score: float,
    ) -> OptimizationIntelligenceEvaluation:
        """
        Generate optimization intelligence evaluation.
        """

        overall_score = (optimization_score + learning_score + evolution_score) / 3.0

        return OptimizationIntelligenceEvaluation(
            overall_score=overall_score,
            optimization_score=optimization_score,
            learning_score=learning_score,
            evolution_score=evolution_score,
        )
