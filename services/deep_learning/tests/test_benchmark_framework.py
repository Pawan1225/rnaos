"""
Tests for benchmark framework integration.
"""

from __future__ import annotations

from dl.benchmark.framework.benchmark_orchestrator import (
    BenchmarkOrchestrator,
)
from dl.benchmark.framework.pipeline_validator import (
    PipelineValidator,
)
from dl.models.benchmark.benchmark_pipeline_config import (
    BenchmarkPipelineConfig,
)


def test_complete_benchmark_framework() -> None:
    """
    Complete benchmark framework lifecycle works.
    """

    config = BenchmarkPipelineConfig(
        config_id="CONFIG_001",
        dataset_id="RFAM_TEST_V1",
        methods=(
            "vienna_rna",
            "rnaos_hybrid",
        ),
        metrics=(
            "structural",
            "energy",
            "performance",
        ),
        enable_statistics=True,
        enable_visualization=True,
        export_formats=(
            "JSON",
            "MARKDOWN",
        ),
        random_seed=42,
        metadata=("version=14.7",),
    )

    validator = PipelineValidator()

    assert validator.validate(
        config,
    )

    orchestrator = BenchmarkOrchestrator()

    pipeline = orchestrator.create_pipeline(
        config,
    )

    assert pipeline.pipeline_id == ("PIPELINE_001")

    assert pipeline.dataset_id == ("RFAM_TEST_V1")

    assert (
        len(
            pipeline.methods,
        )
        == 2
    )

    assert (
        len(
            pipeline.metrics,
        )
        == 3
    )

    assert pipeline.report_id == ("REPORT_001")


def test_invalid_configuration_blocked() -> None:
    """
    Invalid benchmark cannot start.
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
