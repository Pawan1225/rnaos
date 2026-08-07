"""
Tests for pipeline execution engine.
"""

from __future__ import annotations

from dl.models.optimization.optimization_pipeline import (
    OptimizationPipeline,
)
from dl.models.optimization.optimization_stage import (
    OptimizationStage,
)
from dl.models.optimization.pipeline_execution_result import (
    PipelineExecutionResult,
)
from dl.optimization.runtime.pipeline_engine import (
    PipelineExecutionEngine,
)


def test_pipeline_execution() -> None:
    """
    Pipeline executes stages.
    """

    pipeline = OptimizationPipeline(
        pipeline_id=1,
        name="hybrid_rna_pipeline",
        stages=(
            OptimizationStage(
                stage_id=1,
                name="exploration",
                solver_name="genetic",
                priority=1,
                status="pending",
            ),
            OptimizationStage(
                stage_id=2,
                name="optimization",
                solver_name="annealing",
                priority=2,
                status="pending",
            ),
        ),
        status="pending",
    )

    engine = PipelineExecutionEngine()

    result = engine.execute(
        pipeline,
    )

    assert isinstance(
        result,
        PipelineExecutionResult,
    )

    assert result.pipeline_id == 1

    assert result.completed_stages == 2

    assert result.status == ("completed")
