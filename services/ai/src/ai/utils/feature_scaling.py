"""
RNAOS feature scaling utilities.
"""

from __future__ import annotations

import math


def identity_scale(
    value: float,
) -> float:
    """
    Return the value unchanged.
    """
    return value


def z_score_scale(
    value: float,
    mean: float,
    standard_deviation: float,
) -> float:
    """
    Compute a z-score.

    Parameters
    ----------
    value
        Input value.

    mean
        Population mean.

    standard_deviation
        Population standard deviation.

    Returns
    -------
    float
        Standardized value.
    """
    if math.isclose(
        standard_deviation,
        0.0,
    ):
        return 0.0

    return (value - mean) / standard_deviation


def scale_vector(
    values: tuple[float, ...],
    factor: float,
) -> tuple[float, ...]:
    """
    Scale an entire feature vector.
    """
    return tuple(value * factor for value in values)


def l2_norm(
    values: tuple[float, ...],
) -> float:
    """
    Compute the L2 norm.
    """
    return math.sqrt(sum(value * value for value in values))


def l2_normalize(
    values: tuple[float, ...],
) -> tuple[float, ...]:
    """
    Perform L2 normalization.
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


def clip(
    value: float,
    minimum: float,
    maximum: float,
) -> float:
    """
    Clip a value to a specified range.
    """
    return max(
        minimum,
        min(
            value,
            maximum,
        ),
    )
