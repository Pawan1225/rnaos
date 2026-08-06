"""
Tests for intelligence request model.
"""

from __future__ import annotations

from dataclasses import FrozenInstanceError

import pytest
from dl.models.intelligence_configuration import (
    IntelligenceConfiguration,
)
from dl.models.intelligence_request import (
    IntelligenceRequest,
)


def test_request_creation() -> None:
    """
    Request initializes correctly.
    """

    request = IntelligenceRequest(
        sequence="AUGC",
        task="stability_prediction",
        configuration=(IntelligenceConfiguration()),
    )

    assert request.sequence == "AUGC"

    assert request.task == "stability_prediction"

    assert request.configuration.model_family == "transformer"


def test_metadata_support() -> None:
    """
    Metadata is preserved.
    """

    request = IntelligenceRequest(
        sequence="AUGC",
        task="energy_prediction",
        configuration=(IntelligenceConfiguration()),
        metadata=("experiment_001",),
    )

    assert request.metadata == ("experiment_001",)


def test_request_is_immutable() -> None:
    """
    Request cannot change.
    """

    request = IntelligenceRequest(
        sequence="AUGC",
        task="folding",
        configuration=(IntelligenceConfiguration()),
    )

    with pytest.raises(
        FrozenInstanceError,
    ):
        request.sequence = "GGGG"
