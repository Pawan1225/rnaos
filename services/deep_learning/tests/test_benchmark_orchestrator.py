"""
Tests for benchmark orchestrator.
"""

from __future__ import annotations

from dl.benchmark.framework.benchmark_orchestrator import (
    BenchmarkOrchestrator,
)
from dl.models.benchmark.benchmark_pipeline_config import (
    BenchmarkPipelineConfig,
)


def test_create_pipeline() -> None:
    """
    Orchestrator creates pipeline.
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
        ),
        enable_statistics=True,
        enable_visualization=True,
        export_formats=("JSON",),
        random_seed=42,
        metadata=(),
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
