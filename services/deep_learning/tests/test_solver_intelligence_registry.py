"""
Tests for solver intelligence registry.
"""

from __future__ import annotations

from dl.models.optimization.solver_entry import (
    SolverEntry,
)
from dl.models.optimization.solver_registry import (
    SolverRegistry,
)
from dl.optimization.solver_intelligence_registry import (
    SolverIntelligenceRegistry,
)


def test_solver_intelligence_registry() -> None:
    """
    Registry provides solver lookup and selection.
    """

    solver_registry = SolverRegistry(
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
            SolverEntry(
                solver_name="tabu",
                category="local_search",
                capability_score=0.88,
                available=True,
            ),
        ),
        total_solvers=3,
    )

    registry = SolverIntelligenceRegistry(
        solver_registry,
    )

    solver = registry.get_solver("ising")

    assert solver.solver_name == "ising"

    best = registry.best_solver()

    assert best.solver_name == "ising"
    assert best.capability_score == 0.95
