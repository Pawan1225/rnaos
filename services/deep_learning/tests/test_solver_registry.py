"""
Tests for solver registry model.
"""

from __future__ import annotations

from dl.models.optimization.solver_entry import (
    SolverEntry,
)
from dl.models.optimization.solver_registry import (
    SolverRegistry,
)


def test_solver_registry() -> None:
    """
    Solver registry can be created.
    """

    registry = SolverRegistry(
        solvers=(
            SolverEntry(
                solver_name="ising",
                category="quantum",
                capability_score=0.95,
                available=True,
            ),
            SolverEntry(
                solver_name="genetic",
                category="evolutionary",
                capability_score=0.90,
                available=True,
            ),
        ),
        total_solvers=2,
    )

    assert registry.total_solvers == 2

    assert (
        len(
            registry.solvers,
        )
        == 2
    )

    assert registry.solvers[0].solver_name == "ising"

    assert registry.solvers[1].solver_name == "genetic"
