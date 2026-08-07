"""
Tests for objective function engine.
"""

from __future__ import annotations

import pytest
from dl.models.optimization.objective_function import (
    ObjectiveFunction,
)
from dl.optimization.objective_engine import (
    ObjectiveFunctionEngine,
)


def test_create_objective() -> None:
    """
    Objective function is created.
    """

    engine = ObjectiveFunctionEngine()

    objective = engine.create(
        terms=(
            -3.0,
            -2.0,
        ),
    )

    assert isinstance(
        objective,
        ObjectiveFunction,
    )

    assert objective.name == ("rna_energy_minimization")

    assert objective.minimize is True


def test_empty_objective_fails() -> None:
    """
    Empty objective is invalid.
    """

    engine = ObjectiveFunctionEngine()

    with pytest.raises(
        ValueError,
    ):
        engine.create(
            terms=(),
        )
