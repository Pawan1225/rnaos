"""
Tests for intelligence evaluation engine.
"""

from __future__ import annotations

from dl.engines.intelligence_evaluation_engine import (
    IntelligenceEvaluationEngine,
)
from dl.models.intelligence_evaluation import (
    IntelligenceEvaluation,
)


def test_evaluation_calculation() -> None:
    """
    Evaluation calculates error.
    """

    engine = IntelligenceEvaluationEngine()

    result = engine.evaluate(
        predicted=0.8,
        actual=0.7,
    )

    assert isinstance(
        result,
        IntelligenceEvaluation,
    )

    assert result.error == 0.1

    assert result.absolute_error == 0.1


def test_threshold_pass() -> None:
    """
    Prediction passes threshold.
    """

    engine = IntelligenceEvaluationEngine()

    result = engine.evaluate(
        predicted=0.85,
        actual=0.82,
        threshold=0.05,
    )

    assert result.passed_threshold is True
