"""
Tests for benchmark pipeline configuration.
"""

from __future__ import annotations

from dl.models.benchmark.benchmark_pipeline_config import (
    BenchmarkPipelineConfig,
)


def test_benchmark_pipeline_config() -> None:
    """
    Configuration can be created.
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

    assert config.config_id == ("CONFIG_001")

    assert config.dataset_id == ("RFAM_TEST_V1")

    assert config.enable_statistics is True

    assert config.random_seed == 42
