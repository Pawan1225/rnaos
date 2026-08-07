"""
Tests for dataset validator.
"""

from __future__ import annotations

from dl.benchmark.validation.dataset_validator import (
    DatasetValidator,
)
from dl.models.benchmark.benchmark_dataset import (
    BenchmarkDataset,
)


def test_valid_dataset() -> None:
    """
    Valid dataset passes.
    """

    dataset = BenchmarkDataset(
        dataset_id="DATASET_001",
        name="RNA_Benchmark",
        version="1.0",
        samples=(
            "AUGCUA",
            "GGCAUU",
        ),
        source="Rfam",
        status="validated",
    )

    validator = DatasetValidator()

    assert validator.validate(
        dataset,
    )


def test_invalid_sequence() -> None:
    """
    Invalid RNA sequence fails.
    """

    dataset = BenchmarkDataset(
        dataset_id="DATASET_001",
        name="RNA_Benchmark",
        version="1.0",
        samples=("AUGXYZ",),
        source="Rfam",
        status="validated",
    )

    validator = DatasetValidator()

    assert not validator.validate(
        dataset,
    )
