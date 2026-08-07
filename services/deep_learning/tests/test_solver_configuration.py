"""
Tests for solver configuration.
"""

from __future__ import annotations

import pytest
from dl.models.optimization.solver_configuration import (
    SolverConfiguration,
)
from dl.solvers.solver_configuration_validator import (
    SolverConfigurationValidator,
)


def test_valid_configuration() -> None:
    """
    Valid configuration passes.
    """

    config = SolverConfiguration(
        iterations=1000,
        seed=42,
        initial_temperature=10.0,
        cooling_rate=0.95,
        convergence_threshold=0.001,
        checkpoint_interval=100,
    )

    validator = SolverConfigurationValidator()

    assert (
        validator.validate(
            config,
        )
        is True
    )


def test_invalid_iterations() -> None:
    """
    Invalid iterations fail.
    """

    config = SolverConfiguration(
        iterations=0,
        seed=42,
        initial_temperature=10.0,
        cooling_rate=0.95,
        convergence_threshold=0.001,
        checkpoint_interval=100,
    )

    validator = SolverConfigurationValidator()

    with pytest.raises(
        ValueError,
    ):
        validator.validate(
            config,
        )
