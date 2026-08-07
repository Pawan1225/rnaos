"""
Tests for performance metrics.
"""

from __future__ import annotations

from dl.models.benchmark.performance_metrics import (
    PerformanceMetrics,
)


def test_performance_metrics() -> None:
    """
    Performance metrics can be created.
    """

    metrics = PerformanceMetrics(
        runtime=2.43,
        memory_usage=512.0,
        cpu_usage=85.0,
        iterations=1000,
        solver_calls=5,
        scalability_score=0.92,
    )

    assert metrics.runtime == (2.43)

    assert metrics.memory_usage == (512.0)

    assert metrics.cpu_usage == (85.0)

    assert metrics.iterations == (1000)

    assert metrics.solver_calls == (5)

    assert metrics.scalability_score == (0.92)
