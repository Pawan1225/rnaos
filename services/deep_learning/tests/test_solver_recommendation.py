"""
Tests for solver recommendation model.
"""

from __future__ import annotations

from dl.models.optimization.solver_recommendation import (
    SolverRecommendation,
)


def test_solver_recommendation() -> None:
    """
    Solver recommendation can be created.
    """

    recommendation = SolverRecommendation(
        solver="ising",
        confidence=0.95,
        reasoning="Highest capability score",
    )

    assert recommendation.solver == "ising"

    assert recommendation.confidence == 0.95

    assert recommendation.reasoning == "Highest capability score"
