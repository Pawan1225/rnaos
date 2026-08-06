"""
Tests for intelligence configuration.
"""

from __future__ import annotations

from dataclasses import FrozenInstanceError

import pytest
from dl.models.intelligence_configuration import (
    IntelligenceConfiguration,
)


def test_default_configuration() -> None:
    """
    Default intelligence settings.
    """

    configuration = IntelligenceConfiguration()

    assert configuration.model_family == "transformer"

    assert configuration.explanation_enabled is True

    assert configuration.confidence_threshold == 0.5

    assert configuration.execution_mode == "standard"


def test_custom_configuration() -> None:
    """
    Custom intelligence settings.
    """

    configuration = IntelligenceConfiguration(
        model_family="gnn",
        explanation_enabled=False,
        confidence_threshold=0.8,
        execution_mode="gpu",
    )

    assert configuration.model_family == "gnn"

    assert configuration.explanation_enabled is False

    assert configuration.confidence_threshold == 0.8

    assert configuration.execution_mode == "gpu"


def test_configuration_is_immutable() -> None:
    """
    Configuration cannot change.
    """

    configuration = IntelligenceConfiguration()

    with pytest.raises(
        FrozenInstanceError,
    ):
        configuration.model_family = "cnn"
