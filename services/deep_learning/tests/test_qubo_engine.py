"""
Tests for QUBO engine.
"""

from __future__ import annotations

import pytest
from dl.models.optimization.qubo_model import (
    QUBOModel,
)
from dl.optimization.qubo_engine import (
    QUBOEngine,
)


def test_create_qubo_model() -> None:
    """
    QUBO model is created.
    """

    engine = QUBOEngine()

    model = engine.create(
        variables=(
            "x0",
            "x1",
        ),
        matrix=(
            (-2.0, 0.0),
            (0.0, -3.0),
        ),
    )

    assert isinstance(
        model,
        QUBOModel,
    )

    assert model.variables == (
        "x0",
        "x1",
    )


def test_invalid_matrix_size() -> None:
    """
    Invalid QUBO matrix fails.
    """

    engine = QUBOEngine()

    with pytest.raises(
        ValueError,
    ):
        engine.create(
            variables=(
                "x0",
                "x1",
            ),
            matrix=((-1.0,),),
        )
