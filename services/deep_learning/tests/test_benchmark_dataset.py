"""
Tests for benchmark dataset model.
"""

from __future__ import annotations

from dl.models.benchmark.benchmark_dataset import (
    BenchmarkDataset,
)


def test_benchmark_dataset_creation() -> None:
    """
    Benchmark dataset can be created.
    """

    dataset = BenchmarkDataset(
        dataset_id="RNA_DATASET_001",
        name="RNA_Folding_Benchmark",
        version="1.0",
        samples=(
            "AUGCUA",
            "GGCAUU",
        ),
        source="Rfam",
        status="draft",
    )

    assert dataset.dataset_id == ("RNA_DATASET_001")

    assert dataset.name == ("RNA_Folding_Benchmark")

    assert dataset.version == ("1.0")

    assert (
        len(
            dataset.samples,
        )
        == 2
    )

    assert dataset.source == ("Rfam")

    assert dataset.status == ("draft")
