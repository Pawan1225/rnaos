"""
Tests for adaptive solver selector.
"""

from __future__ import annotations

from dl.models.optimization.adaptive_solver_selection import (
    AdaptiveSolverSelection,
)
from dl.optimization.adaptive_solver_selector import (
    AdaptiveSolverSelector,
)


def test_complex_problem_selects_annealing() -> None:
    """
    Complex problems prioritize annealing.
    """

    selector = AdaptiveSolverSelector()

    result = selector.select(
        sequence_length=100,
        complexity=0.9,
        constraint_density=0.2,
    )

    assert isinstance(
        result,
        AdaptiveSolverSelection,
    )

    assert result.primary_solver == ("annealing")


def test_large_problem_selects_tensor() -> None:
    """
    Large problems prioritize tensor.
    """

    selector = AdaptiveSolverSelector()

    result = selector.select(
        sequence_length=1000,
        complexity=0.4,
        constraint_density=0.2,
    )

    assert result.primary_solver == ("tensor")
