"""
Tests for benchmark dataset subsystem.
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


def create_dataset(
    dataset_id: str = "DATASET_001",
) -> BenchmarkDataset:
    """
    Create valid benchmark dataset.
    """

    return BenchmarkDataset(
        dataset_id=dataset_id,
        name="RNA_Benchmark",
        version="1.0",
        samples=(
            "AUGCUA",
            "GGCAUU",
        ),
        source="Rfam",
        status="validated",
    )


def test_dataset_registration_and_retrieval() -> None:
    """
    Registered dataset can be retrieved.
    """

    manager = DatasetManager(
        DatasetValidator(),
    )

    dataset = create_dataset()

    assert manager.register(
        dataset,
    )

    result = manager.get(
        "DATASET_001",
    )

    assert result == dataset


def test_invalid_sequence_rejected() -> None:
    """
    Invalid RNA sequence fails.
    """

    manager = DatasetManager(
        DatasetValidator(),
    )

    dataset = BenchmarkDataset(
        dataset_id="INVALID_001",
        name="Invalid",
        version="1.0",
        samples=("AUGXYZ",),
        source="Test",
        status="validated",
    )

    assert not manager.register(
        dataset,
    )


def test_empty_dataset_rejected() -> None:
    """
    Empty dataset fails.
    """

    manager = DatasetManager(
        DatasetValidator(),
    )

    dataset = BenchmarkDataset(
        dataset_id="EMPTY_001",
        name="Empty",
        version="1.0",
        samples=(),
        source="Test",
        status="validated",
    )

    assert not manager.register(
        dataset,
    )


def test_duplicate_dataset_replaces_existing() -> None:
    """
    Dataset registry handles duplicate IDs.
    """

    manager = DatasetManager(
        DatasetValidator(),
    )

    first = create_dataset()

    second = BenchmarkDataset(
        dataset_id="DATASET_001",
        name="Updated_RNA_Benchmark",
        version="2.0",
        samples=("AUGC",),
        source="Rfam",
        status="validated",
    )

    assert manager.register(
        first,
    )

    assert manager.register(
        second,
    )

    result = manager.get(
        "DATASET_001",
    )

    assert result == second
