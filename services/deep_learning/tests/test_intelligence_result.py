"""
Tests for intelligence result model.
"""

from __future__ import annotations

from dataclasses import FrozenInstanceError

import pytest
from dl.models.explanation_report import (
    ExplanationReport,
)
from dl.models.intelligence_result import (
    IntelligenceResult,
)
from dl.models.prediction_result import (
    PredictionResult,
)


def create_prediction() -> PredictionResult:
    """
    Create test prediction.
    """

    return PredictionResult(
        prediction_task="stability",
        value=0.85,
        confidence=0.9,
    )


def test_result_creation() -> None:
    """
    Intelligence result initializes.
    """

    result = IntelligenceResult(
        prediction=create_prediction(),
        explanation=None,
        selected_model="transformer",
        confidence=0.9,
        completed=True,
    )

    assert result.selected_model == "transformer"

    assert result.confidence == 0.9

    assert result.completed is True


def test_explanation_support() -> None:
    """
    Explanation can be attached.
    """

    report = ExplanationReport(
        prediction_task="stability",
        prediction_value=0.85,
        explanations=(),
        confidence=0.8,
        completed=True,
    )

    result = IntelligenceResult(
        prediction=create_prediction(),
        explanation=report,
        selected_model="transformer",
        confidence=0.8,
        completed=True,
    )

    assert result.explanation == report


def test_result_is_immutable() -> None:
    """
    Result cannot change.
    """

    result = IntelligenceResult(
        prediction=create_prediction(),
        explanation=None,
        selected_model="cnn",
        confidence=0.5,
        completed=True,
    )

    with pytest.raises(
        FrozenInstanceError,
    ):
        result.selected_model = "gnn"
