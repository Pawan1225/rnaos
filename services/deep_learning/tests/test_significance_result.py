"""
Tests for significance result.
"""

from __future__ import annotations

from dl.models.benchmark.significance_result import (
    SignificanceResult,
)


def test_significance_result() -> None:
    """
    Significance result can be created.
    """

    result = SignificanceResult(
        test_name="t_test",
        p_value=0.002,
        alpha=0.05,
        significant=True,
        sample_size=1000,
    )

    assert result.test_name == ("t_test")

    assert result.p_value == 0.002

    assert result.alpha == 0.05

    assert result.significant is True

    assert result.sample_size == 1000
