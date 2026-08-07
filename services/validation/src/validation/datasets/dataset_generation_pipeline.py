"""
RNA benchmark dataset generation pipeline.
"""

from __future__ import annotations

import random

from validation.models.dataset_entry import (
    DatasetEntry,
)


class DatasetGenerationPipeline:
    """
    Generates reproducible RNA datasets.
    """

    NUCLEOTIDES = (
        "A",
        "U",
        "C",
        "G",
    )

    def generate(
        self,
        length: int,
        count: int,
        category: str,
        seed: int = 42,
    ) -> tuple[DatasetEntry, ...]:
        """
        Generate RNA benchmark samples.
        """

        rng = random.Random(seed)

        entries = []

        for index in range(count):
            sequence = "".join(
                rng.choice(
                    self.NUCLEOTIDES,
                )
                for _ in range(length)
            )

            entries.append(
                DatasetEntry(
                    sequence_id=(f"{category}_{index}"),
                    sequence=sequence,
                    length=length,
                    category=category,
                    seed=seed,
                    metadata=(
                        "synthetic",
                        "public_data",
                    ),
                )
            )

        return tuple(entries)
