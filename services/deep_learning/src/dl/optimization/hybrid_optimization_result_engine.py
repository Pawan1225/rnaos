"""
RNAOS hybrid optimization result engine.
"""

from __future__ import annotations

from dl.models.optimization.hybrid_optimization_result import (
    HybridOptimizationResult,
)
from dl.models.optimization.parallel_coordination_result import (
    ParallelCoordinationResult,
)


class HybridOptimizationResultEngine:
    """
    Builds the final hybrid optimization result.
    """

    def build(
        self,
        strategy_name: str,
        parallel_result: ParallelCoordinationResult,
        confidence: float,
    ) -> HybridOptimizationResult:
        """
        Create the hybrid optimization result.
        """

        if not parallel_result.executed_solvers:
            raise ValueError(
                "At least one solver must execute",
            )

        return HybridOptimizationResult(
            strategy_name=strategy_name,
            executed_solvers=parallel_result.executed_solvers,
            status=("completed" if parallel_result.success else "failed"),
            best_solver=parallel_result.executed_solvers[0],
            confidence=confidence,
        )
