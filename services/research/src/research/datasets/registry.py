from __future__ import annotations

from collections.abc import Callable

from research.datasets.benchmark_dataset import BenchmarkDataset
from research.datasets.toy import load_toy_dataset
from research.models.dataset_info import DatasetInfo


class DatasetRegistry:
    """
    Registry of available benchmark datasets.
    """

    def __init__(self) -> None:
        self._loaders: dict[
            str,
            Callable[[], BenchmarkDataset],
        ] = {}

        self._metadata: dict[
            str,
            DatasetInfo,
        ] = {}

    def register(
        self,
        *,
        info: DatasetInfo,
        loader: Callable[[], BenchmarkDataset],
    ) -> None:
        self._loaders[info.name] = loader
        self._metadata[info.name] = info

    def load(self, name: str) -> BenchmarkDataset:
        return self._loaders[name]()

    def list(self) -> list[DatasetInfo]:
        return sorted(
            self._metadata.values(),
            key=lambda x: x.name,
        )


registry = DatasetRegistry()

registry.register(
    info=DatasetInfo(
        name="toy",
        version="1.0",
        description="Synthetic benchmark dataset",
        source="RNAOS",
    ),
    loader=load_toy_dataset,
)
