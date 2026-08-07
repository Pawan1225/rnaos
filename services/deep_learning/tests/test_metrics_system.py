"""
Tests for evaluation metrics system.
"""

from __future__ import annotations

from dl.models.benchmark.energy_metrics import (
    EnergyMetrics,
)
from dl.models.benchmark.evaluation_metrics import (
    EvaluationMetrics,
)
from dl.models.benchmark.performance_metrics import (
    PerformanceMetrics,
)
from dl.models.benchmark.structural_metrics import (
    StructuralMetrics,
)


def test_complete_metrics_pipeline() -> None:
    """
    Complete evaluation metrics pipeline works.
    """

    structural = StructuralMetrics(
        base_pair_accuracy=0.95,
        sensitivity=0.94,
        specificity=0.96,
        precision=0.93,
        recall=0.94,
        f1_score=0.935,
    )

    energy = EnergyMetrics(
        reference_energy=-30.0,
        predicted_energy=-34.0,
        energy_gap=4.0,
        relative_error=0.13,
        improvement=0.13,
    )

    performance = PerformanceMetrics(
        runtime=1.5,
        memory_usage=256.0,
        cpu_usage=70.0,
        iterations=500,
        solver_calls=3,
        scalability_score=0.90,
    )

    evaluation = EvaluationMetrics(
        structural=structural,
        energy=energy,
        performance=performance,
    )

    assert evaluation.structural.f1_score > 0.9

    assert evaluation.energy.improvement > 0

    assert evaluation.performance.runtime > 0


def test_metric_ranges() -> None:
    """
    Metric values remain within expected ranges.
    """

    structural = StructuralMetrics(
        base_pair_accuracy=1.0,
        sensitivity=1.0,
        specificity=1.0,
        precision=1.0,
        recall=1.0,
        f1_score=1.0,
    )

    assert 0.0 <= structural.f1_score <= 1.0
