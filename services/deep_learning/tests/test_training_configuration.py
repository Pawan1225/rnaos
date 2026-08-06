"""
Tests for training configuration.
"""

from __future__ import annotations

from dataclasses import FrozenInstanceError

import pytest
from dl.models.training_configuration import (
    TrainingConfiguration,
)


def test_default_configuration() -> None:
    """
    Default training configuration.
    """

    configuration = TrainingConfiguration()

    assert configuration.epochs == 10

    assert configuration.batch_size == 32

    assert configuration.learning_rate == 0.001

    assert configuration.optimizer == "adam"


def test_custom_configuration() -> None:
    """
    Custom values are accepted.
    """

    configuration = TrainingConfiguration(
        epochs=50,
        batch_size=64,
    )

    assert configuration.epochs == 50

    assert configuration.batch_size == 64


def test_configuration_is_immutable() -> None:
    """
    Configuration cannot be modified.
    """

    configuration = TrainingConfiguration()

    with pytest.raises(
        FrozenInstanceError,
    ):
        configuration.epochs = 100
