"""
Tests for benchmark dataset manager.
"""

from validation.datasets.benchmark_dataset_manager import (
    BenchmarkDatasetManager,
)


def test_dataset_generation() -> None:
    """
    Dataset generation works.
    """

    manager = BenchmarkDatasetManager()

    dataset = manager.generate(
        count=5,
        length=20,
        seed=42,
    )

    assert dataset.dataset_id == ("RNA_BENCHMARK_001")

    assert (
        len(
            dataset.sequences,
        )
        == 5
    )

    assert dataset.sequence_lengths == (
        20,
        20,
        20,
        20,
        20,
    )

    assert dataset.random_seed == 42
