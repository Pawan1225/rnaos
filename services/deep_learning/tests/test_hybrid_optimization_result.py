"""
Tests for hybrid optimization result model.
"""

from __future__ import annotations

from dl.models.optimization.hybrid_optimization_result import (
    HybridOptimizationResult,
)
from dl.models.optimization.optimization_candidate import (
    OptimizationCandidate,
)
from dl.models.optimization.result_comparison import (
    ResultComparison,
)


def test_hybrid_optimization_result() -> None:
    """
    Hybrid optimization result can be created.
    """

    candidate = OptimizationCandidate(
        candidate_id=1,
        solver_name="ising",
        fitness=0.95,
        quality=0.90,
    )

    comparison = ResultComparison(
        candidates=(candidate,),
        best_candidate=candidate,
        comparison_metric="fitness",
    )

    result = HybridOptimizationResult(
        strategy_name="hybrid",
        executed_solvers=(
            "ising",
            "genetic",
            "tabu",
        ),
        status="completed",
        best_solver=comparison.best_candidate.solver_name,
        confidence=0.95,
    )

    assert isinstance(
        result,
        HybridOptimizationResult,
    )

    assert result.strategy_name == "hybrid"

    assert result.best_solver == "ising"

    assert result.executed_solvers == (
        "ising",
        "genetic",
        "tabu",
    )

    assert result.status == "completed"

    assert result.confidence == 0.95
