"""
Tests for optimization intelligence evaluation engine.
"""

from __future__ import annotations

from dl.models.optimization.optimization_intelligence_evaluation import (
    OptimizationIntelligenceEvaluation,
)
from dl.optimization.optimization_intelligence_evaluation_engine import (
    OptimizationIntelligenceEvaluationEngine,
)


def test_optimization_intelligence_evaluation() -> None:
    """
    Optimization intelligence evaluation works.
    """

    engine = OptimizationIntelligenceEvaluationEngine()

    result = engine.evaluate(
        optimization_score=0.95,
        learning_score=0.90,
        evolution_score=0.85,
    )

    assert isinstance(
        result,
        OptimizationIntelligenceEvaluation,
    )

    assert result.overall_score == 0.9

    assert result.optimization_score == 0.95

    assert result.learning_score == 0.90

    assert result.evolution_score == 0.85
