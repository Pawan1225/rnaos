"""
RNAOS benchmark dataset validator.
"""

from __future__ import annotations

from dl.models.benchmark.benchmark_dataset import (
    BenchmarkDataset,
)


class DatasetValidator:
    """
    Validates benchmark datasets.
    """

    VALID_STATUS = (
        "draft",
        "validated",
        "active",
    )

    VALID_BASES = {
        "A",
        "U",
        "G",
        "C",
    }

    def validate(
        self,
        dataset: BenchmarkDataset,
    ) -> bool:
        """
        Validate benchmark dataset.
        """

        if not dataset.dataset_id:
            return False

        if not dataset.name:
            return False

        if not dataset.version:
            return False

        if not dataset.source:
            return False

        if not dataset.samples:
            return False

        if dataset.status not in self.VALID_STATUS:
            return False

        for sample in dataset.samples:
            if not sample:
                return False

            if not set(sample).issubset(
                self.VALID_BASES,
            ):
                return False

        return True
