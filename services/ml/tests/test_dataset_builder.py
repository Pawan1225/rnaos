"""
Tests for the RNAOS dataset builder.
"""

from __future__ import annotations

import pytest
from ai.models.feature_vector import (
    FeatureVector,
)
from ml.analyzers.dataset_builder import (
    DatasetBuilder,
)
from ml.models.ml_dataset import (
    MLDataset,
)


@pytest.fixture
def builder() -> DatasetBuilder:
    """Create dataset builder."""
    return DatasetBuilder()


@pytest.fixture
def feature_vectors() -> tuple[FeatureVector, ...]:
    """Create deterministic feature vectors."""
    names = (
        "gc_content",
        "complexity",
        "embedding_score",
    )

    return (
        FeatureVector(
            feature_names=names,
            values=(
                0.50,
                0.30,
                0.80,
            ),
            dimension=len(names),
        ),
        FeatureVector(
            feature_names=names,
            values=(
                0.60,
                0.40,
                0.70,
            ),
            dimension=len(names),
        ),
        FeatureVector(
            feature_names=names,
            values=(
                0.40,
                0.20,
                0.90,
            ),
            dimension=len(names),
        ),
        FeatureVector(
            feature_names=names,
            values=(
                0.55,
                0.35,
                0.75,
            ),
            dimension=len(names),
        ),
    )


@pytest.fixture
def dataset(
    builder: DatasetBuilder,
    feature_vectors: tuple[FeatureVector, ...],
) -> MLDataset:
    """Create ML dataset."""
    return builder.build(
        feature_vectors,
        (
            0.10,
            0.20,
            0.30,
            0.40,
        ),
    )


def test_dataset_creation(
    dataset: MLDataset,
) -> None:
    """Dataset should be created."""
    assert dataset is not None


def test_sample_count(
    dataset: MLDataset,
) -> None:
    """Sample count should match."""
    assert dataset.sample_count == 4


def test_feature_count(
    dataset: MLDataset,
) -> None:
    """Feature count should match."""
    assert dataset.feature_count == 3


def test_dataset_version_exists(
    dataset: MLDataset,
) -> None:
    """Dataset version should exist."""
    assert dataset.dataset_version != ""


def test_train_validation_test_split(
    dataset: MLDataset,
) -> None:
    """Dataset split should cover all samples."""
    total = dataset.train_size + dataset.validation_size + dataset.test_size

    assert total == dataset.sample_count


def test_feature_matrix_size(
    dataset: MLDataset,
) -> None:
    """Feature matrix should contain one row per sample."""
    assert (
        len(
            dataset.features,
        )
        == dataset.sample_count
    )


def test_targets_size(
    dataset: MLDataset,
) -> None:
    """Target vector should match sample count."""
    assert (
        len(
            dataset.targets,
        )
        == dataset.sample_count
    )


def test_deterministic_build(
    builder: DatasetBuilder,
    feature_vectors: tuple[FeatureVector, ...],
) -> None:
    """Dataset creation should be deterministic."""
    targets = (
        0.10,
        0.20,
        0.30,
        0.40,
    )

    first = builder.build(
        feature_vectors,
        targets,
    )

    second = builder.build(
        feature_vectors,
        targets,
    )

    assert first == second


def test_invalid_targets(
    builder: DatasetBuilder,
    feature_vectors: tuple[FeatureVector, ...],
) -> None:
    """Mismatched targets should fail."""
    with pytest.raises(
        ValueError,
    ):
        builder.build(
            feature_vectors,
            (
                1.0,
                2.0,
            ),
        )


def test_dataset_is_immutable(
    dataset: MLDataset,
) -> None:
    """Dataset should be immutable."""
    with pytest.raises(
        AttributeError,
    ):
        dataset.targets = ()
