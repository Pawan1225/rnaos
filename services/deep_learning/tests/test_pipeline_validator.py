"""
Tests for pipeline validator.
"""

from __future__ import annotations

from dl.benchmark.framework.pipeline_validator import (
    PipelineValidator,
)
from dl.models.benchmark.benchmark_pipeline_config import (
    BenchmarkPipelineConfig,
)


def test_valid_pipeline_configuration() -> None:
    """
    Valid configuration passes.
    """

    config = BenchmarkPipelineConfig(
        config_id="CONFIG_001",
        dataset_id="RFAM_TEST_V1",
        methods=(
            "vienna_rna",
            "rnaos_hybrid",
        ),
        metrics=(
            "energy",
            "structural",
        ),
        enable_statistics=True,
        enable_visualization=True,
        export_formats=("JSON",),
        random_seed=42,
        metadata=(),
    )

    validator = PipelineValidator()

    assert validator.validate(
        config,
    )


def test_invalid_pipeline_configuration() -> None:
    """
    Invalid configuration fails.
    """

    config = BenchmarkPipelineConfig(
        config_id="",
        dataset_id="",
        methods=(),
        metrics=(),
        enable_statistics=False,
        enable_visualization=False,
        export_formats=(),
        random_seed=42,
        metadata=(),
    )

    validator = PipelineValidator()

    assert not validator.validate(
        config,
    )
