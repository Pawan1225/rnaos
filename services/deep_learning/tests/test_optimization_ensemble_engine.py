"""
Tests for optimization ensemble engine.
"""

from __future__ import annotations

import pytest
from dl.models.optimization.ensemble_result import (
    EnsembleResult,
)
from dl.optimization.optimization_ensemble_engine import (
    OptimizationEnsembleEngine,
)


def test_best_candidate_selected() -> None:
    """
    Lowest energy candidate wins.
    """

    engine = OptimizationEnsembleEngine()

    result = engine.select_best(
        candidates=(
            (
                "qubo",
                -10.0,
            ),
            (
                "annealing",
                -15.0,
            ),
            (
                "tensor",
                -12.0,
            ),
        ),
    )

    assert isinstance(
        result,
        EnsembleResult,
    )

    assert result.selected_solver == ("annealing")

    assert result.energy == -15.0


def test_empty_candidates_fail() -> None:
    """
    Empty candidate list fails.
    """

    engine = OptimizationEnsembleEngine()

    with pytest.raises(
        ValueError,
    ):
        engine.select_best(
            candidates=(),
        )
