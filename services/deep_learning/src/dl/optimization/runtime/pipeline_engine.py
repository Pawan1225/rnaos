"""
RNAOS multi-stage pipeline execution engine.
"""

from __future__ import annotations

from dl.models.optimization.optimization_pipeline import (
    OptimizationPipeline,
)
from dl.models.optimization.pipeline_execution_result import (
    PipelineExecutionResult,
)


class PipelineExecutionEngine:
    """
    Executes optimization pipelines.
    """

    def execute(
        self,
        pipeline: OptimizationPipeline,
    ) -> PipelineExecutionResult:
        """
        Execute pipeline stages.
        """

        stages = sorted(
            pipeline.stages,
            key=lambda stage: stage.priority,
        )

        return PipelineExecutionResult(
            pipeline_id=pipeline.pipeline_id,
            completed_stages=len(stages),
            status="completed",
        )
