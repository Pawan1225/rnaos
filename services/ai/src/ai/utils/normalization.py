"""
RNAOS feature normalization utilities.
"""

from __future__ import annotations

import math


def min_max_normalize(
    value: float,
    minimum: float,
    maximum: float,
) -> float:
    """
    Perform min-max normalization.

    Parameters
    ----------
    value
        Input value.

    minimum
        Minimum allowable value.

    maximum
        Maximum allowable value.

    Returns
    -------
    float
        Normalized value in the range [0.0, 1.0].
    """
    if math.isclose(
        minimum,
        maximum,
    ):
        return 0.0

    normalized = (value - minimum) / (maximum - minimum)

    return max(
        0.0,
        min(
            normalized,
            1.0,
        ),
    )


def normalize_ratio(
    value: float,
) -> float:
    """
    Normalize a ratio value.

    Ratios are expected to already lie within
    the interval [0.0, 1.0].
    """
    return max(
        0.0,
        min(
            value,
            1.0,
        ),
    )


def safe_divide(
    numerator: float,
    denominator: float,
) -> float:
    """
    Safely divide two values.

    Returns
    -------
    float
        Zero when the denominator is zero.
    """
    if math.isclose(
        denominator,
        0.0,
    ):
        return 0.0

    return numerator / denominator


def validate_feature(
    value: float,
) -> float:
    """
    Validate a feature value.

    Raises
    ------
    ValueError
        If the feature is NaN or infinite.
    """
    if math.isnan(value):
        raise ValueError(
            "Feature value cannot be NaN.",
        )

    if math.isinf(value):
        raise ValueError(
            "Feature value cannot be infinite.",
        )

    return value


def validate_features(
    values: tuple[float, ...],
) -> tuple[float, ...]:
    """
    Validate every feature value.
    """
    return tuple(validate_feature(value) for value in values)
