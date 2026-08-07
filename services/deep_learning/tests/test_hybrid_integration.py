"""
Tests for hybrid optimization integration.
"""

from __future__ import annotations

from dl.models.optimization.hybrid_optimization_request import (
    HybridOptimizationRequest,
)
from dl.models.optimization.hybrid_solution import (
    HybridSolution,
)
from dl.models.optimization.optimization_pipeline import (
    OptimizationPipeline,
)
from dl.models.optimization.optimization_stage import (
    OptimizationStage,
)
from dl.optimization.runtime.hybrid_optimizer import (
    HybridOptimizationEngine,
)


def test_hybrid_integration() -> None:
    """
    Complete hybrid optimization flow works.
    """

    stage = OptimizationStage(
        stage_id=1,
        name="exploration",
        solver_name="genetic",
        priority=1,
        status="pending",
    )

    pipeline = OptimizationPipeline(
        pipeline_id=1,
        name="hybrid_pipeline",
        stages=(stage,),
        status="pending",
    )

    request = HybridOptimizationRequest(
        request_id=1,
        problem_id="rna_001",
        pipeline=pipeline,
        target_accuracy=0.95,
        priority=1,
        status="pending",
    )

    engine = HybridOptimizationEngine()

    solution = engine.optimize(
        request,
    )

    assert isinstance(
        solution,
        HybridSolution,
    )

    assert solution.success is True

    assert solution.objective_score == 0.95
