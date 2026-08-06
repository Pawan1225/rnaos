"""
Tests for confidence estimator.
"""

from __future__ import annotations

from dl.engines.confidence_estimator import (
    ConfidenceEstimator,
)


def test_confidence_estimation() -> None:
    """
    Confidence is calculated.
    """

    estimator = ConfidenceEstimator()

    confidence = estimator.estimate(
        0.85,
    )

    assert confidence == 0.85


def test_confidence_upper_bound() -> None:
    """
    Confidence cannot exceed one.
    """

    estimator = ConfidenceEstimator()

    confidence = estimator.estimate(
        5.0,
    )

    assert confidence == 1.0


def test_confidence_lower_bound() -> None:
    """
    Confidence cannot be negative.
    """

    estimator = ConfidenceEstimator()

    confidence = estimator.estimate(
        -5.0,
    )

    assert confidence == 1.0
