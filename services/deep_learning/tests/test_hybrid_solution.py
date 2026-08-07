"""
Tests for hybrid solution model.
"""

from __future__ import annotations

from dl.models.optimization.hybrid_solution import (
    HybridSolution,
)


def test_hybrid_solution_creation() -> None:
    """
    Hybrid solution can be created.
    """

    solution = HybridSolution(
        solution_id=1,
        strategy_name="quantum_evolutionary",
        objective_score=0.97,
        success=True,
    )

    assert solution.solution_id == 1

    assert solution.strategy_name == ("quantum_evolutionary")

    assert solution.objective_score == 0.97

    assert solution.success is True
