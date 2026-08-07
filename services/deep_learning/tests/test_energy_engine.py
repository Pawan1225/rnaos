"""
Tests for energy evaluation engine.
"""

from __future__ import annotations

import pytest
from dl.models.optimization.energy_result import (
    EnergyResult,
)
from dl.models.optimization.q_matrix import (
    QMatrix,
)
from dl.optimization.energy_engine import (
    EnergyEvaluationEngine,
)


def test_energy_calculation() -> None:
    """
    QUBO energy is calculated.
    """

    engine = EnergyEvaluationEngine()

    matrix = QMatrix(
        variables=(
            "x0",
            "x1",
        ),
        values=(
            (
                -3.0,
                0.0,
            ),
            (
                0.0,
                -2.0,
            ),
        ),
    )

    result = engine.evaluate(
        matrix,
        (
            1,
            1,
        ),
    )

    assert isinstance(
        result,
        EnergyResult,
    )

    assert result.energy == -5.0


def test_invalid_state_dimension() -> None:
    """
    Invalid state fails.
    """

    engine = EnergyEvaluationEngine()

    matrix = QMatrix(
        variables=("x0",),
        values=((-1.0,),),
    )

    with pytest.raises(
        ValueError,
    ):
        engine.evaluate(
            matrix,
            (
                1,
                0,
            ),
        )
