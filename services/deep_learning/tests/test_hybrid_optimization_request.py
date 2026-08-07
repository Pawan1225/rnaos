"""
Tests for hybrid optimization request.
"""

from __future__ import annotations

from dl.models.optimization.hybrid_optimization_request import (
    HybridOptimizationRequest,
)
from dl.models.optimization.optimization_pipeline import (
    OptimizationPipeline,
)
from dl.models.optimization.optimization_stage import (
    OptimizationStage,
)


def test_hybrid_optimization_request() -> None:
    """
    Request can be created.
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

    assert request.request_id == 1

    assert request.problem_id == ("rna_001")

    assert request.pipeline.pipeline_id == 1

    assert request.target_accuracy == 0.95

    assert request.priority == 1

    assert request.status == ("pending")
