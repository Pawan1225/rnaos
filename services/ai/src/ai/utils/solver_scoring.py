"""
RNAOS solver recommendation scoring utilities.
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


def weighted_score(
    values: tuple[float, ...],
    weights: tuple[float, ...],
) -> float:
    """
    Compute a weighted score.
    """
    if len(values) != len(weights):
        raise ValueError(
            "Values and weights must have equal length.",
        )

    total_weight = sum(
        weights,
    )

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


def affinity_score(
    *,
    complexity: float,
    stability: float,
    quantum_suitability: float,
) -> float:
    """
    Compute a normalized solver affinity score.
    """
    return clamp(
        weighted_score(
            (
                complexity,
                stability,
                quantum_suitability,
            ),
            (
                0.4,
                0.3,
                0.3,
            ),
        ),
    )


def runtime_score(
    *,
    optimization_difficulty: float,
    search_space_complexity: float,
) -> float:
    """
    Estimate normalized runtime complexity.
    """
    return clamp(
        (optimization_difficulty + search_space_complexity) / 2.0,
    )


def confidence_score(
    *,
    classical: float,
    quantum: float,
    hybrid: float,
) -> float:
    """
    Estimate recommendation confidence.

    Higher confidence is assigned when one
    solver family is clearly favored.
    """
    spread = max(
        classical,
        quantum,
        hybrid,
    ) - min(
        classical,
        quantum,
        hybrid,
    )

    return clamp(
        0.5 + spread / 2.0,
    )
