"""
Tests for confidence interval.
"""

from __future__ import annotations

from dl.models.benchmark.confidence_interval import (
    ConfidenceInterval,
)


def test_confidence_interval() -> None:
    """
    Confidence interval can be created.
    """

    interval = ConfidenceInterval(
        confidence_level=0.95,
        lower_bound=0.905,
        upper_bound=0.935,
        margin_of_error=0.015,
    )

    assert interval.confidence_level == 0.95

    assert interval.lower_bound == 0.905

    assert interval.upper_bound == 0.935

    assert interval.margin_of_error == 0.015
