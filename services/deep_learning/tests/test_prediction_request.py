"""
Tests for prediction request model.
"""

from __future__ import annotations

from dataclasses import FrozenInstanceError

import pytest
from dl.models.prediction_request import (
    PredictionRequest,
)


def test_prediction_request_creation() -> None:
    """
    Prediction request initializes correctly.
    """

    request = PredictionRequest(
        sequence="AUGCGGAU",
        prediction_task="folding_difficulty",
    )

    assert request.sequence == "AUGCGGAU"

    assert request.prediction_task == "folding_difficulty"

    assert request.model_version == "v1"


def test_custom_prediction_request() -> None:
    """
    Custom values are accepted.
    """

    request = PredictionRequest(
        sequence="AUGC",
        prediction_task="stability",
        model_version="v2",
        metadata=("experiment_001",),
    )

    assert request.model_version == "v2"

    assert request.metadata == ("experiment_001",)


def test_request_is_immutable() -> None:
    """
    Request cannot be modified.
    """

    request = PredictionRequest(
        sequence="AUGC",
        prediction_task="energy",
    )

    with pytest.raises(
        FrozenInstanceError,
    ):
        request.sequence = "GGGG"
