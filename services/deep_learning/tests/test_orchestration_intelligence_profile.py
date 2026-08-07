"""
Tests for orchestration intelligence profile.
"""

from __future__ import annotations

from dl.models.optimization.orchestration_feature import (
    OrchestrationFeature,
)
from dl.models.optimization.orchestration_intelligence_profile import (
    OrchestrationIntelligenceProfile,
)
from dl.models.optimization.orchestration_metrics import (
    OrchestrationMetrics,
)


def test_orchestration_intelligence_profile() -> None:
    """
    Orchestration intelligence profile can be created.
    """

    feature = OrchestrationFeature(
        feature_name="parallel_efficiency",
        value=0.95,
        category="orchestration",
    )

    metrics = OrchestrationMetrics(
        executed_solvers=3,
        successful_executions=3,
        average_confidence=0.94,
        parallel_tasks=2,
    )

    profile = OrchestrationIntelligenceProfile(
        features=(feature,),
        metrics=metrics,
        confidence=0.95,
    )

    assert len(profile.features) == 1

    assert profile.metrics.executed_solvers == 3

    assert profile.metrics.parallel_tasks == 2

    assert profile.confidence == 0.95
