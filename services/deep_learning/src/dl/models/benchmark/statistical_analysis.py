"""
RNAOS statistical analysis model.
"""

from __future__ import annotations

from dataclasses import dataclass

from dl.models.benchmark.confidence_interval import (
    ConfidenceInterval,
)
from dl.models.benchmark.effect_size import (
    EffectSize,
)
from dl.models.benchmark.significance_result import (
    SignificanceResult,
)
from dl.models.benchmark.statistical_summary import (
    StatisticalSummary,
)


@dataclass(
    slots=True,
    frozen=True,
)
class StatisticalAnalysis:
    """
    Complete statistical analysis result.
    """

    summary: StatisticalSummary

    confidence: ConfidenceInterval

    effect_size: EffectSize

    significance: SignificanceResult
