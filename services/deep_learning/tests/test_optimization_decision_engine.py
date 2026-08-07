"""
Tests for optimization decision engine.
"""

from __future__ import annotations

from dl.models.optimization.optimization_decision import (
    OptimizationDecision,
)
from dl.optimization.optimization_decision_engine import (
    OptimizationDecisionEngine,
)


def test_large_sequence_decision() -> None:
    """
    Large sequences select tensor.
    """

    engine = OptimizationDecisionEngine()

    result = engine.decide(
        sequence_length=1000,
        complexity=0.5,
        folding_difficulty=0.5,
    )

    assert isinstance(
        result,
        OptimizationDecision,
    )

    assert result.strategy == "tensor"


def test_complex_landscape_decision() -> None:
    """
    Complex problems select annealing.
    """

    engine = OptimizationDecisionEngine()

    result = engine.decide(
        sequence_length=100,
        complexity=0.9,
        folding_difficulty=0.5,
    )

    assert result.strategy == "annealing"
