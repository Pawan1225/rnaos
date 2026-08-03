from __future__ import annotations

from research.datasets.registry import registry


def load_dataset(name: str):
    return registry.load(name)


def available_datasets():
    return registry.list()
