"""
Tests for statistical summary.
"""

from __future__ import annotations

from dl.models.benchmark.statistical_summary import (
    StatisticalSummary,
)


def test_statistical_summary() -> None:
    """
    Summary can be created.
    """

    summary = StatisticalSummary(
        mean=0.90,
        median=0.92,
        standard_deviation=0.05,
        variance=0.0025,
        minimum=0.70,
        maximum=0.99,
        sample_size=100,
    )

    assert summary.mean == 0.90

    assert summary.median == 0.92

    assert summary.standard_deviation == 0.05

    assert summary.variance == 0.0025

    assert summary.minimum == 0.70

    assert summary.maximum == 0.99

    assert summary.sample_size == 100
