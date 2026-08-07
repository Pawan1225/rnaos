"""
Tests for optimization pipeline.
"""

from __future__ import annotations

from dl.models.optimization.optimization_pipeline import (
    OptimizationPipeline,
)
from dl.models.optimization.optimization_stage import (
    OptimizationStage,
)


def test_optimization_pipeline() -> None:
    """
    Pipeline stores optimization stages.
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
        name="hybrid_rna_pipeline",
        stages=(stage,),
        status="pending",
    )

    assert pipeline.pipeline_id == 1

    assert pipeline.name == ("hybrid_rna_pipeline")

    assert (
        len(
            pipeline.stages,
        )
        == 1
    )

    assert pipeline.status == ("pending")
