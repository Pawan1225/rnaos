"""
RNAOS feature selection utilities.
"""

from __future__ import annotations

from ai.models.feature_vector import (
    FeatureVector,
)


def variance_scores(
    feature_vector: FeatureVector,
) -> tuple[float, ...]:
    """
    Compute simple feature scores.

    Currently uses absolute feature magnitude as a
    deterministic baseline.

    This utility is intentionally simple and will
    evolve into true statistical feature selection
    (variance thresholding, mutual information,
    recursive feature elimination, etc.).
    """
    return tuple(abs(value) for value in feature_vector.values)


def select_top_features(
    feature_vector: FeatureVector,
    scores: tuple[float, ...],
    top_k: int,
) -> tuple[
    tuple[int, ...],
    tuple[str, ...],
    tuple[float, ...],
]:
    """
    Select the top-k highest-scoring features.
    """
    ranked = sorted(
        enumerate(scores),
        key=lambda item: item[1],
        reverse=True,
    )

    selected = ranked[:top_k]

    indices = tuple(index for index, _ in selected)

    names = tuple(feature_vector.feature_names[index] for index in indices)

    selected_scores = tuple(score for _, score in selected)

    return (
        indices,
        names,
        selected_scores,
    )


def validate_top_k(
    feature_count: int,
    top_k: int,
) -> None:
    """
    Validate requested feature count.
    """
    if top_k <= 0:
        raise ValueError(
            "top_k must be greater than zero.",
        )

    if top_k > feature_count:
        raise ValueError(
            "top_k cannot exceed feature count.",
        )
