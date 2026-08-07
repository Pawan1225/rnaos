"""
Tests for ensemble result model.
"""

from __future__ import annotations

from dl.models.optimization.ensemble_result import (
    EnsembleResult,
)


def test_ensemble_result_creation() -> None:
    """
    Ensemble result can be created.
    """

    result = EnsembleResult(
        selected_solver="ising",
        energy=-45.2,
        candidate_count=3,
    )

    assert result.selected_solver == ("ising")

    assert result.energy == -45.2

    assert result.candidate_count == 3
