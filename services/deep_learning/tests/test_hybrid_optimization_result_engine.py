"""
Tests for hybrid optimization result engine.
"""

from __future__ import annotations

from dl.models.optimization.hybrid_optimization_result import (
    HybridOptimizationResult,
)
from dl.models.optimization.parallel_coordination_result import (
    ParallelCoordinationResult,
)
from dl.optimization.hybrid_optimization_result_engine import (
    HybridOptimizationResultEngine,
)


def test_hybrid_optimization_result() -> None:
    """
    Hybrid optimization result is generated.
    """

    engine = HybridOptimizationResultEngine()

    parallel_result = ParallelCoordinationResult(
        total_tasks=3,
        completed_tasks=3,
        executed_solvers=(
            "ising",
            "genetic",
            "tabu",
        ),
        success=True,
    )

    result = engine.build(
        strategy_name="hybrid",
        parallel_result=parallel_result,
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
