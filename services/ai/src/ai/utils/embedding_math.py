"""
RNAOS embedding mathematics utilities.
"""

from __future__ import annotations

import math


def l2_norm(
    values: tuple[float, ...],
) -> float:
    """
    Compute the Euclidean (L2) norm.
    """
    return math.sqrt(sum(value * value for value in values))


def normalize_embedding(
    values: tuple[float, ...],
) -> tuple[float, ...]:
    """
    Normalize an embedding using the L2 norm.

    Returns
    -------
    tuple[float, ...]
        Unit-length embedding.
    """
    norm = l2_norm(
        values,
    )

    if math.isclose(
        norm,
        0.0,
    ):
        return values

    return tuple(value / norm for value in values)


def dot_product(
    left: tuple[float, ...],
    right: tuple[float, ...],
) -> float:
    """
    Compute the dot product between two embeddings.
    """
    if len(left) != len(right):
        raise ValueError(
            "Embeddings must have equal dimension.",
        )

    return sum(
        a * b
        for a, b in zip(
            left,
            right,
            strict=True,
        )
    )


def cosine_similarity(
    left: tuple[float, ...],
    right: tuple[float, ...],
) -> float:
    """
    Compute cosine similarity between two embeddings.
    """
    left_norm = l2_norm(
        left,
    )

    right_norm = l2_norm(
        right,
    )

    if math.isclose(
        left_norm,
        0.0,
    ) or math.isclose(
        right_norm,
        0.0,
    ):
        return 0.0

    return dot_product(
        left,
        right,
    ) / (left_norm * right_norm)


def euclidean_distance(
    left: tuple[float, ...],
    right: tuple[float, ...],
) -> float:
    """
    Compute Euclidean distance between two embeddings.
    """
    if len(left) != len(right):
        raise ValueError(
            "Embeddings must have equal dimension.",
        )

    return math.sqrt(
        sum(
            (a - b) ** 2
            for a, b in zip(
                left,
                right,
                strict=True,
            )
        )
    )
