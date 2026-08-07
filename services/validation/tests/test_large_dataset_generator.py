"""
Tests for large dataset generator.
"""

from validation.datasets.large_dataset_generator import (
    LargeDatasetGenerator,
)


def test_large_dataset_generation():

    generator = LargeDatasetGenerator()

    dataset = generator.generate(
        samples_per_length=10,
        seed=42,
    )

    assert dataset.dataset_id == ("RNAOS_BENCHMARK_DATASET_V2")

    assert dataset.total_sequences == 40

    assert dataset.sequence_lengths == (
        20,
        40,
        60,
        80,
    )

    assert dataset.version == ("1.0.0")
