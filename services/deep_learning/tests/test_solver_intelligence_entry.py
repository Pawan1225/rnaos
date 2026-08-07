"""
Tests for solver intelligence entry model.
"""

from __future__ import annotations

from dl.models.optimization.solver_intelligence_entry import (
    SolverIntelligenceEntry,
)


def test_solver_intelligence_entry() -> None:
    """
    Solver intelligence entry can be created.
    """

    entry = SolverIntelligenceEntry(
        solver_name="ising",
        category="quantum",
        capability_score=0.95,
        enabled=True,
    )

    assert entry.solver_name == "ising"

    assert entry.category == "quantum"

    assert entry.capability_score == 0.95

    assert entry.enabled is True
