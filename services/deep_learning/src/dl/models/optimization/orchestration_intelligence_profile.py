"""
RNAOS orchestration intelligence profile model.
"""

from __future__ import annotations

from dataclasses import dataclass

from dl.models.optimization.orchestration_feature import (
    OrchestrationFeature,
)
from dl.models.optimization.orchestration_metrics import (
    OrchestrationMetrics,
)


@dataclass(
    slots=True,
    frozen=True,
)
class OrchestrationIntelligenceProfile:
    """
    Immutable orchestration intelligence profile.
    """

    features: tuple[
        OrchestrationFeature,
        ...,
    ]

    metrics: OrchestrationMetrics

    confidence: float
