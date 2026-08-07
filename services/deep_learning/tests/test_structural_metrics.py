"""
Tests for structural metrics.
"""

from __future__ import annotations

from dl.models.benchmark.structural_metrics import (
    StructuralMetrics,
)


def test_structural_metrics() -> None:
    """
    Structural metrics can be created.
    """

    metrics = StructuralMetrics(
        base_pair_accuracy=0.92,
        sensitivity=0.90,
        specificity=0.95,
        precision=0.91,
        recall=0.90,
        f1_score=0.905,
    )

    assert metrics.base_pair_accuracy == (0.92)

    assert metrics.sensitivity == (0.90)

    assert metrics.specificity == (0.95)

    assert metrics.precision == (0.91)

    assert metrics.recall == (0.90)

    assert metrics.f1_score == (0.905)
