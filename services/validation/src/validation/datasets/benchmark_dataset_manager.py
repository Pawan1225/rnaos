"""
RNAOS benchmark dataset manager.
"""

from __future__ import annotations

import random

from validation.models.benchmark_dataset import (
    BenchmarkDataset,
)


class BenchmarkDatasetManager:
    """
    Creates reproducible RNA datasets.
    """

    NUCLEOTIDES = (
        "A",
        "U",
        "C",
        "G",
    )

    def generate(
        self,
        count: int,
        length: int,
        seed: int = 42,
    ) -> BenchmarkDataset:
        """
        Generate synthetic RNA sequences.
        """

        rng = random.Random(seed)

        sequences = tuple(
            "".join(
                rng.choice(
                    self.NUCLEOTIDES,
                )
                for _ in range(length)
            )
            for _ in range(count)
        )

        return BenchmarkDataset(
            dataset_id="RNA_BENCHMARK_001",
            version="1.0.0",
            sequences=sequences,
            sequence_lengths=tuple(length for _ in sequences),
            source="synthetic_random",
            random_seed=seed,
            metadata=(
                "public_data_only",
                "reproducible_generation",
            ),
        )
