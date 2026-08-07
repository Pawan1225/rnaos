"""
RNAOS benchmark orchestrator.
"""

from __future__ import annotations

from dl.models.benchmark.benchmark_pipeline import (
    BenchmarkPipeline,
)
from dl.models.benchmark.benchmark_pipeline_config import (
    BenchmarkPipelineConfig,
)


class BenchmarkOrchestrator:
    """
    Coordinates scientific benchmark execution.
    """

    def create_pipeline(
        self,
        config: BenchmarkPipelineConfig,
    ) -> BenchmarkPipeline:
        """
        Create benchmark pipeline state.
        """

        return BenchmarkPipeline(
            pipeline_id="PIPELINE_001",
            experiment_id="EXP_001",
            dataset_id=config.dataset_id,
            methods=config.methods,
            metrics=config.metrics,
            statistics=("STATISTICAL_ANALYSIS",),
            visualizations=("VISUALIZATION_REPORT",),
            report_id="REPORT_001",
            metadata=("created_by=orchestrator",),
        )
