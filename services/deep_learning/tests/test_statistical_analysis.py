"""
Tests for statistical analysis.
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


def test_statistical_analysis() -> None:
    """
    Complete analysis can be created.
    """

    analysis = StatisticalAnalysis(
        summary=StatisticalSummary(
            mean=0.90,
            median=0.92,
            standard_deviation=0.05,
            variance=0.0025,
            minimum=0.70,
            maximum=0.99,
            sample_size=100,
        ),
        confidence=ConfidenceInterval(
            confidence_level=0.95,
            lower_bound=0.88,
            upper_bound=0.92,
            margin_of_error=0.02,
        ),
        effect_size=EffectSize(
            cohens_d=0.8,
            improvement_ratio=0.15,
            relative_gain=15.0,
        ),
        significance=SignificanceResult(
            test_name="t_test",
            p_value=0.002,
            alpha=0.05,
            significant=True,
            sample_size=100,
        ),
    )

    assert analysis.summary.mean == 0.90

    assert analysis.confidence.confidence_level == 0.95

    assert analysis.effect_size.cohens_d == 0.8

    assert analysis.significance.significant is True
