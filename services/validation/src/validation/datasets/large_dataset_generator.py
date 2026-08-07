"""
RNAOS large benchmark dataset generator.
"""

from __future__ import annotations

from validation.datasets.dataset_generation_pipeline import (
    DatasetGenerationPipeline,
)
from validation.models.large_dataset import (
    LargeBenchmarkDataset,
)


class LargeDatasetGenerator:
    """
    Generates RNAOS large benchmark datasets.
    """

    def generate(
        self,
        samples_per_length: int = 100,
        seed: int = 42,
    ) -> LargeBenchmarkDataset:
        """
        Generate complete benchmark dataset.
        """

        pipeline = DatasetGenerationPipeline()

        entries = []

        lengths = (
            20,
            40,
            60,
            80,
        )

        for length in lengths:
            dataset = pipeline.generate(
                length=length,
                count=samples_per_length,
                category=f"RNA_{length}",
                seed=seed,
            )

            entries.extend(dataset)

        return LargeBenchmarkDataset(
            dataset_id=("RNAOS_BENCHMARK_DATASET_V2"),
            total_sequences=len(entries),
            sequence_lengths=lengths,
            entries=tuple(entries),
            version="1.0.0",
        )
