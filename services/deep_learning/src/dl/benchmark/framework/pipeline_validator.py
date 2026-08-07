"""
RNAOS benchmark pipeline validator.
"""

from __future__ import annotations

from dl.models.benchmark.benchmark_pipeline_config import (
    BenchmarkPipelineConfig,
)


class PipelineValidator:
    """
    Validates benchmark configurations.
    """

    def validate(
        self,
        config: BenchmarkPipelineConfig,
    ) -> bool:
        """
        Validate benchmark configuration.
        """

        if not config.config_id:
            return False

        if not config.dataset_id:
            return False

        if not config.methods:
            return False

        if not config.metrics:
            return False

        if config.random_seed is None:
            return False

        return bool(
            config.export_formats,
        )
