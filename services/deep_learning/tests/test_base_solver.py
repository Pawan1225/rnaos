"""
Tests for quantum-inspired solver interface.
"""

from __future__ import annotations

import pytest
from dl.solvers.base_solver import (
    BaseQuantumInspiredSolver,
)


class DummySolver(
    BaseQuantumInspiredSolver,
):
    """
    Test solver implementation.
    """

    def solve(
        self,
        problem,
    ) -> tuple[int, ...]:
        return (
            1,
            0,
        )

    def name(
        self,
    ) -> str:
        return "dummy"


def test_solver_interface() -> None:
    """
    Solver follows interface.
    """

    solver = DummySolver()

    assert solver.name() == "dummy"

    assert solver.solve(
        None,
    ) == (
        1,
        0,
    )


def test_interface_is_abstract() -> None:
    """
    Base solver cannot instantiate.
    """

    with pytest.raises(
        TypeError,
    ):
        BaseQuantumInspiredSolver()
