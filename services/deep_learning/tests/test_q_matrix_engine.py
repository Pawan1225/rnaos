"""
Tests for Q matrix engine.
"""

from __future__ import annotations

import pytest
from dl.models.optimization.q_matrix import (
    QMatrix,
)
from dl.optimization.q_matrix_engine import (
    QMatrixConstructionEngine,
)


def test_create_q_matrix() -> None:
    """
    Q matrix is created.
    """

    engine = QMatrixConstructionEngine()

    matrix = engine.create(
        variables=(
            "x0",
            "x1",
        ),
        diagonal_terms=(
            -3.0,
            -2.0,
        ),
    )

    assert isinstance(
        matrix,
        QMatrix,
    )

    assert matrix.values == (
        (
            -3.0,
            0.0,
        ),
        (
            0.0,
            -2.0,
        ),
    )


def test_invalid_dimensions() -> None:
    """
    Invalid dimensions fail.
    """

    engine = QMatrixConstructionEngine()

    with pytest.raises(
        ValueError,
    ):
        engine.create(
            variables=("x0",),
            diagonal_terms=(
                -1.0,
                -2.0,
            ),
        )
