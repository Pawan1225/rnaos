"""
Tests for hybrid configuration.
"""

from __future__ import annotations

import pytest
from dl.models.optimization.hybrid_configuration import (
    HybridConfiguration,
)
from dl.optimization.hybrid_validator import (
    HybridConfigurationValidator,
)


def test_valid_hybrid_configuration() -> None:
    """
    Valid configuration passes.
    """

    config = HybridConfiguration(
        enable_qubo=True,
        enable_annealing=True,
        enable_tensor=True,
        ensemble_mode="adaptive",
        max_solvers=3,
        selection_strategy="energy",
    )

    validator = HybridConfigurationValidator()

    assert (
        validator.validate(
            config,
        )
        is True
    )


def test_no_solver_enabled() -> None:
    """
    Empty configuration fails.
    """

    config = HybridConfiguration(
        enable_qubo=False,
        enable_annealing=False,
        enable_tensor=False,
        ensemble_mode="none",
        max_solvers=3,
        selection_strategy="energy",
    )

    validator = HybridConfigurationValidator()

    with pytest.raises(
        ValueError,
    ):
        validator.validate(
            config,
        )
