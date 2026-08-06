"""
RNAOS meta feature mathematics utilities.
"""

from __future__ import annotations


def clamp(
    value: float,
    *,
    minimum: float = 0.0,
    maximum: float = 1.0,
) -> float:
    """
    Clamp a value to a specified range.
    """
    return max(
        minimum,
        min(
            value,
            maximum,
        ),
    )


def weighted_average(
    values: tuple[float, ...],
    weights: tuple[float, ...],
) -> float:
    """
    Compute a weighted average.
    """
    if len(values) != len(weights):
        raise ValueError(
            "Values and weights must have equal length.",
        )

    total_weight = sum(weights)

    if total_weight == 0.0:
        return 0.0

    return (
        sum(
            value * weight
            for value, weight in zip(
                values,
                weights,
                strict=True,
            )
        )
        / total_weight
    )


def interaction_score(
    first: float,
    second: float,
) -> float:
    """
    Compute a normalized interaction score.
    """
    return clamp(
        (first + second) / 2.0,
    )


def complexity_score(
    *,
    complexity: float,
    stem_density: float,
    motif_density: float,
) -> float:
    """
    Compute a composite structural complexity score.
    """
    return weighted_average(
        (
            complexity,
            stem_density,
            motif_density,
        ),
        (
            0.5,
            0.3,
            0.2,
        ),
    )


def readiness_score(
    *,
    stability: float,
    complexity: float,
    quantum_suitability: float,
) -> float:
    """
    Compute an overall AI readiness score.
    """
    return weighted_average(
        (
            stability,
            complexity,
            quantum_suitability,
        ),
        (
            0.4,
            0.3,
            0.3,
        ),
    )
