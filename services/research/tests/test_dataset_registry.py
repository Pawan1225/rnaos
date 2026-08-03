from research.datasets.loader import (
    available_datasets,
    load_dataset,
)


def test_load_toy_dataset():
    dataset = load_dataset("toy")

    assert len(dataset) == 3


def test_registry_contains_toy():
    names = {dataset.name for dataset in available_datasets()}

    assert "toy" in names
