"""
Tests for prediction result model.
"""

from __future__ import annotations

from dataclasses import FrozenInstanceError

import pytest
from dl.models.prediction_result import (
    PredictionResult,
)


def test_prediction_result_creation() -> None:
    """
    Prediction result initializes correctly.
    """

    result = PredictionResult(
        prediction_task="folding_difficulty",
        value=0.75,
        confidence=0.92,
    )

    assert result.prediction_task == "folding_difficulty"

    assert result.value == 0.75

    assert result.confidence == 0.92

    assert result.model_version == "v1"


def test_custom_prediction_result() -> None:
    """
    Custom prediction values work.
    """

    result = PredictionResult(
        prediction_task="stability",
        value=0.88,
        model_version="v2",
        metadata=("experiment_001",),
    )

    assert result.model_version == "v2"

    assert result.metadata == ("experiment_001",)


def test_prediction_result_is_immutable() -> None:
    """
    Result cannot be modified.
    """

    result = PredictionResult(
        prediction_task="energy",
        value=1.0,
    )

    with pytest.raises(
        FrozenInstanceError,
    ):
        result.value = 2.0
