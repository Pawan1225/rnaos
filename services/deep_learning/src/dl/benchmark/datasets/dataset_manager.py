"""
RNAOS benchmark dataset manager.
"""

from __future__ import annotations

from dl.benchmark.validation.dataset_validator import (
    DatasetValidator,
)
from dl.models.benchmark.benchmark_dataset import (
    BenchmarkDataset,
)


class DatasetManager:
    """
    Manages benchmark datasets.
    """

    def __init__(
        self,
        validator: DatasetValidator,
    ) -> None:
        self._validator = validator

        self._datasets: dict[
            str,
            BenchmarkDataset,
        ] = {}

    def register(
        self,
        dataset: BenchmarkDataset,
    ) -> bool:
        """
        Register benchmark dataset.
        """

        if not self._validator.validate(
            dataset,
        ):
            return False

        self._datasets[dataset.dataset_id] = dataset

        return True

    def get(
        self,
        dataset_id: str,
    ) -> BenchmarkDataset | None:
        """
        Retrieve benchmark dataset.
        """

        return self._datasets.get(
            dataset_id,
        )
