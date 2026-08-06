"""
Tests for explanation configuration.
"""

from __future__ import annotations

from dataclasses import FrozenInstanceError

import pytest
from dl.models.explanation_configuration import (
    ExplanationConfiguration,
)


def test_default_configuration() -> None:
    """
    Default explanation settings.
    """

    configuration = ExplanationConfiguration()

    assert configuration.method == "saliency"

    assert configuration.top_features == 10

    assert configuration.attribution_threshold == 0.5

    assert configuration.generate_visualization is True


def test_custom_configuration() -> None:
    """
    Custom explanation settings.
    """

    configuration = ExplanationConfiguration(
        method="integrated_gradients",
        top_features=20,
        include_attention=True,
    )

    assert configuration.method == "integrated_gradients"

    assert configuration.top_features == 20

    assert configuration.include_attention is True


def test_configuration_is_immutable() -> None:
    """
    Configuration cannot be changed.
    """

    configuration = ExplanationConfiguration()

    with pytest.raises(
        FrozenInstanceError,
    ):
        configuration.method = "attention"
