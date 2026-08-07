"""
Tests for solver recommendation engine.
"""

from __future__ import annotations

from dl.models.optimization.solver_recommendation import (
    SolverRecommendation,
)
from dl.optimization.solver_recommendation_engine import (
    SolverRecommendationEngine,
)


def test_large_sequence_uses_tensor() -> None:
    """
    Large RNA sequences use tensor optimization.
    """

    engine = SolverRecommendationEngine()

    result = engine.recommend(
        sequence_length=1000,
        complexity=0.5,
        constraint_density=0.2,
    )

    assert isinstance(
        result,
        SolverRecommendation,
    )

    assert result.solver == "tensor"


def test_complex_problem_uses_annealing() -> None:
    """
    Complex landscapes use annealing.
    """

    engine = SolverRecommendationEngine()

    result = engine.recommend(
        sequence_length=100,
        complexity=0.9,
        constraint_density=0.2,
    )

    assert result.solver == "annealing"
