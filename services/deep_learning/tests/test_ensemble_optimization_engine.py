"""
Tests for ensemble optimization engine.
"""

from __future__ import annotations

from dl.models.optimization.ensemble_result import (
    EnsembleResult,
)
from dl.models.optimization.solver_candidate import (
    SolverCandidate,
)
from dl.optimization.runtime.ensemble_engine import (
    EnsembleOptimizationEngine,
)


def test_ensemble_optimization() -> None:
    """
    Engine selects best candidate.
    """

    candidates = (
        SolverCandidate(
            candidate_id=1,
            source_solver="ising",
            structure=(
                "A",
                "U",
            ),
            energy=-40.0,
            score=0.90,
        ),
        SolverCandidate(
            candidate_id=2,
            source_solver="genetic",
            structure=(
                "A",
                "U",
                "G",
            ),
            energy=-45.0,
            score=0.95,
        ),
    )

    engine = EnsembleOptimizationEngine()

    result = engine.optimize(
        candidates,
    )

    assert isinstance(
        result,
        EnsembleResult,
    )

    assert result.selected_candidate.source_solver == ("genetic")

    assert result.confidence == 0.95

    assert result.status == ("completed")
