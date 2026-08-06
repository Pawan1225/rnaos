"""
Tests for inference configuration.
"""

from __future__ import annotations

from dataclasses import FrozenInstanceError

import pytest
from dl.models.inference_configuration import (
    InferenceConfiguration,
)


def test_default_configuration() -> None:
    """
    Default inference configuration.
    """

    configuration = InferenceConfiguration()

    assert configuration.model_version == "v1"

    assert configuration.device == "cpu"

    assert configuration.batch_size == 1

    assert configuration.deterministic is True


def test_custom_configuration() -> None:
    """
    Custom inference values.
    """

    configuration = InferenceConfiguration(
        model_version="v2",
        device="gpu",
        batch_size=16,
    )

    assert configuration.model_version == "v2"

    assert configuration.device == "gpu"

    assert configuration.batch_size == 16


def test_configuration_is_immutable() -> None:
    """
    Configuration cannot change.
    """

    configuration = InferenceConfiguration()

    with pytest.raises(
        FrozenInstanceError,
    ):
        configuration.device = "gpu"
