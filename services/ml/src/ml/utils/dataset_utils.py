"""
RNAOS dataset utility functions.
"""

from __future__ import annotations

from ai.models.feature_vector import (
    FeatureVector,
)

DEFAULT_TRAIN_RATIO = 0.70
DEFAULT_VALIDATION_RATIO = 0.15


def build_feature_matrix(
    feature_vectors: tuple[
        FeatureVector,
        ...,
    ],
) -> tuple[
    tuple[float, ...],
    ...,
]:
    """
    Convert feature vectors into a feature matrix.
    """
    return tuple(vector.values for vector in feature_vectors)


def validate_targets(
    targets: tuple[
        float,
        ...,
    ],
    sample_count: int,
) -> None:
    """
    Validate target vector.
    """
    if (
        len(
            targets,
        )
        != sample_count
    ):
        raise ValueError(
            "Target count must equal sample count.",
        )


def deterministic_split(
    sample_count: int,
    train_ratio: float = DEFAULT_TRAIN_RATIO,
    validation_ratio: float = DEFAULT_VALIDATION_RATIO,
) -> tuple[
    tuple[int, ...],
    tuple[int, ...],
    tuple[int, ...],
]:
    """
    Deterministically split dataset indices into
    train, validation, and test sets.
    """
    train_end = int(
        sample_count * train_ratio,
    )

    validation_end = train_end + int(
        sample_count * validation_ratio,
    )

    train = tuple(
        range(
            train_end,
        ),
    )

    validation = tuple(
        range(
            train_end,
            validation_end,
        ),
    )

    test = tuple(
        range(
            validation_end,
            sample_count,
        ),
    )

    return (
        train,
        validation,
        test,
    )


def dataset_version(
    feature_count: int,
    sample_count: int,
) -> str:
    """
    Generate deterministic dataset version.
    """
    return f"ml-v1-{sample_count}x{feature_count}"
