"""
Tests for Ising engine.
"""

from __future__ import annotations

from dl.models.optimization.ising_model import (
    IsingModel,
)
from dl.models.optimization.qubo_model import (
    QUBOModel,
)
from dl.optimization.ising_engine import (
    IsingEngine,
)


def test_qubo_to_ising_conversion() -> None:
    """
    QUBO converts to Ising.
    """

    engine = IsingEngine()

    qubo = QUBOModel(
        variables=(
            "x0",
            "x1",
        ),
        matrix=(
            (-2.0, 0.0),
            (0.0, -3.0),
        ),
    )

    ising = engine.from_qubo(
        qubo,
    )

    assert isinstance(
        ising,
        IsingModel,
    )

    assert ising.variables == (
        "x0",
        "x1",
    )


def test_ising_dimensions() -> None:
    """
    Ising dimensions match variables.
    """

    engine = IsingEngine()

    qubo = QUBOModel(
        variables=("bp_1",),
        matrix=((-1.0,),),
    )

    ising = engine.from_qubo(
        qubo,
    )

    assert (
        len(
            ising.local_fields,
        )
        == 1
    )

    assert (
        len(
            ising.couplings,
        )
        == 1
    )
