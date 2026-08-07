"""
Tests for orchestration metrics model.
"""

from __future__ import annotations

from dl.models.optimization.orchestration_metrics import (
    OrchestrationMetrics,
)


def test_orchestration_metrics() -> None:
    """
    Orchestration metrics can be created.
    """

    metrics = OrchestrationMetrics(
        executed_solvers=3,
        successful_executions=3,
        average_confidence=0.94,
        parallel_tasks=2,
    )

    assert metrics.executed_solvers == 3

    assert metrics.successful_executions == 3

    assert metrics.average_confidence == 0.94

    assert metrics.parallel_tasks == 2
