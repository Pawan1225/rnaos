"""
Tests for dataset manager.
"""

from __future__ import annotations

from dl.benchmark.datasets.dataset_manager import (
    DatasetManager,
)
from dl.benchmark.validation.dataset_validator import (
    DatasetValidator,
)
from dl.models.benchmark.benchmark_dataset import (
    BenchmarkDataset,
)


def test_dataset_registration() -> None:
    """
    Dataset can be registered.
    """

    manager = DatasetManager(
        DatasetValidator(),
    )

    dataset = BenchmarkDataset(
        dataset_id="DATASET_001",
        name="RNA_Benchmark",
        version="1.0",
        samples=("AUGCUA",),
        source="Rfam",
        status="validated",
    )

    result = manager.register(
        dataset,
    )

    assert result is True

    stored = manager.get(
        "DATASET_001",
    )

    assert stored is not None

    assert stored.name == ("RNA_Benchmark")
