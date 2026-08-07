"""
Tests for statistical analysis system.
"""

from __future__ import annotations

from dl.models.benchmark.confidence_interval import (
    ConfidenceInterval,
)
from dl.models.benchmark.effect_size import (
    EffectSize,
)
from dl.models.benchmark.significance_result import (
    SignificanceResult,
)
from dl.models.benchmark.statistical_analysis import (
    StatisticalAnalysis,
)
from dl.models.benchmark.statistical_summary import (
    StatisticalSummary,
)


def test_complete_statistics_pipeline() -> None:
    """
    Complete statistical pipeline works.
    """

    analysis = StatisticalAnalysis(
        summary=StatisticalSummary(
            mean=0.92,
            median=0.93,
            standard_deviation=0.03,
            variance=0.0009,
            minimum=0.80,
            maximum=0.99,
            sample_size=1000,
        ),
        confidence=ConfidenceInterval(
            confidence_level=0.95,
            lower_bound=0.90,
            upper_bound=0.94,
            margin_of_error=0.02,
        ),
        effect_size=EffectSize(
            cohens_d=1.1,
            improvement_ratio=0.20,
            relative_gain=20.0,
        ),
        significance=SignificanceResult(
            test_name="t_test",
            p_value=0.001,
            alpha=0.05,
            significant=True,
            sample_size=1000,
        ),
    )

    assert analysis.summary.sample_size == 1000

    assert analysis.confidence.confidence_level == 0.95

    assert analysis.effect_size.cohens_d > 0

    assert analysis.significance.significant is True


def test_confidence_range() -> None:
    """
    Confidence interval remains valid.
    """

    interval = ConfidenceInterval(
        confidence_level=0.95,
        lower_bound=0.90,
        upper_bound=0.94,
        margin_of_error=0.02,
    )

    assert interval.lower_bound < interval.upper_bound
