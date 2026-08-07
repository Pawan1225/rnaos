"""
Tests for quantum-inspired configuration.
"""

from __future__ import annotations

import pytest
from dl.models.optimization.quantum_inspired_configuration import (
    QuantumInspiredConfiguration,
)
from dl.optimization.quantum_inspired_validator import (
    QuantumInspiredConfigurationValidator,
)


def test_valid_configuration() -> None:
    """
    Valid configuration passes.
    """

    config = QuantumInspiredConfiguration(
        enable_qubo=True,
        enable_annealing=True,
        enable_tensor=True,
        enable_hybrid=True,
        optimization_mode="adaptive",
        seed=42,
    )

    validator = QuantumInspiredConfigurationValidator()

    assert (
        validator.validate(
            config,
        )
        is True
    )


def test_no_optimizer_enabled() -> None:
    """
    Empty configuration fails.
    """

    config = QuantumInspiredConfiguration(
        enable_qubo=False,
        enable_annealing=False,
        enable_tensor=False,
        enable_hybrid=False,
        optimization_mode="none",
        seed=42,
    )

    validator = QuantumInspiredConfigurationValidator()

    with pytest.raises(
        ValueError,
    ):
        validator.validate(
            config,
        )
