"""
RNAOS machine learning dataset model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class MLDataset:
    """
    Immutable machine learning dataset.

    Stores feature matrices, targets, dataset metadata,
    and train/validation/test partitions used by the
    Machine Learning Engine.
    """

    feature_names: tuple[str, ...]

    features: tuple[tuple[float, ...], ...]

    targets: tuple[float, ...]

    train_indices: tuple[int, ...]

    validation_indices: tuple[int, ...]

    test_indices: tuple[int, ...]

    dataset_version: str

    @property
    def sample_count(
        self,
    ) -> int:
        """
        Number of samples.
        """
        return len(
            self.features,
        )

    @property
    def feature_count(
        self,
    ) -> int:
        """
        Number of features.
        """
        return len(
            self.feature_names,
        )

    @property
    def train_size(
        self,
    ) -> int:
        """
        Number of training samples.
        """
        return len(
            self.train_indices,
        )

    @property
    def validation_size(
        self,
    ) -> int:
        """
        Number of validation samples.
        """
        return len(
            self.validation_indices,
        )

    @property
    def test_size(
        self,
    ) -> int:
        """
        Number of test samples.
        """
        return len(
            self.test_indices,
        )
