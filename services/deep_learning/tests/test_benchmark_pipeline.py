"""
Tests for benchmark pipeline.
"""

from __future__ import annotations

from dl.models.benchmark.benchmark_pipeline import (
    BenchmarkPipeline,
)


def test_benchmark_pipeline() -> None:
    """
    Pipeline model can be created.
    """

    pipeline = BenchmarkPipeline(
        pipeline_id="PIPELINE_001",
        experiment_id="EXP_001",
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
        statistics=("STAT_001",),
        visualizations=("VIS_REPORT_001",),
        report_id="REPORT_001",
        metadata=("version=14.7",),
    )

    assert pipeline.pipeline_id == ("PIPELINE_001")

    assert pipeline.dataset_id == ("RFAM_TEST_V1")

    assert (
        len(
            pipeline.methods,
        )
        == 2
    )

    assert pipeline.report_id == ("REPORT_001")
