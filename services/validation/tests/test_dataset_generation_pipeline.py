"""
Tests for dataset generation pipeline.
"""

from validation.datasets.dataset_generation_pipeline import (
    DatasetGenerationPipeline,
)


def test_dataset_generation() -> None:
    """
    Dataset generation works.
    """

    pipeline = DatasetGenerationPipeline()

    dataset = pipeline.generate(
        length=20,
        count=5,
        category="RNA_20",
        seed=42,
    )

    assert len(dataset) == 5

    assert dataset[0].length == 20

    assert dataset[0].category == ("RNA_20")

    assert dataset[0].metadata[0] == "synthetic"
