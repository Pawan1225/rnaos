"""
RNAOS machine learning dataset builder.
"""

from __future__ import annotations

from ai.models.feature_vector import (
    FeatureVector,
)
from ml.models.ml_dataset import (
    MLDataset,
)
from ml.utils.dataset_utils import (
    build_feature_matrix,
    dataset_version,
    deterministic_split,
    validate_targets,
)


class DatasetBuilder:
    """
    Construct immutable machine learning datasets.

    Converts AI-generated feature vectors into a
    deterministic dataset suitable for downstream
    machine learning components.
    """

    def build(
        self,
        feature_vectors: tuple[
            FeatureVector,
            ...,
        ],
        targets: tuple[
            float,
            ...,
        ],
    ) -> MLDataset:
        """
        Build an immutable ML dataset.
        """
        feature_matrix = build_feature_matrix(
            feature_vectors,
        )

        validate_targets(
            targets,
            len(feature_matrix),
        )

        (
            train_indices,
            validation_indices,
            test_indices,
        ) = deterministic_split(
            len(feature_matrix),
        )

        feature_names = feature_vectors[0].feature_names if feature_vectors else ()

        version = dataset_version(
            feature_count=len(feature_names),
            sample_count=len(feature_matrix),
        )

        return MLDataset(
            feature_names=feature_names,
            features=feature_matrix,
            targets=targets,
            train_indices=train_indices,
            validation_indices=validation_indices,
            test_indices=test_indices,
            dataset_version=version,
        )
