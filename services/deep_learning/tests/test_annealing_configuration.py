"""
Tests for annealing configuration.
"""

from __future__ import annotations

import pytest
from dl.models.optimization.annealing_configuration import (
    AnnealingConfiguration,
)
from dl.solvers.annealing_validator import (
    AnnealingConfigurationValidator,
)


def test_valid_annealing_configuration() -> None:
    """
    Valid configuration passes.
    """

    config = AnnealingConfiguration(
        initial_temperature=10.0,
        minimum_temperature=0.01,
        cooling_rate=0.95,
        iterations=1000,
        seed=42,
    )

    validator = AnnealingConfigurationValidator()

    assert (
        validator.validate(
            config,
        )
        is True
    )


def test_invalid_temperature() -> None:
    """
    Invalid temperature fails.
    """

    config = AnnealingConfiguration(
        initial_temperature=-1.0,
        minimum_temperature=0.01,
        cooling_rate=0.95,
        iterations=100,
        seed=42,
    )

    validator = AnnealingConfigurationValidator()

    with pytest.raises(
        ValueError,
    ):
        validator.validate(
            config,
        )
