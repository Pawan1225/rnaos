"""
Tests for evaluation metrics.
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


def test_evaluation_metrics() -> None:
    """
    Evaluation metrics combine all measurements.
    """

    structural = StructuralMetrics(
        base_pair_accuracy=0.92,
        sensitivity=0.90,
        specificity=0.95,
        precision=0.91,
        recall=0.90,
        f1_score=0.905,
    )

    energy = EnergyMetrics(
        reference_energy=-32.5,
        predicted_energy=-35.1,
        energy_gap=2.6,
        relative_error=0.08,
        improvement=0.08,
    )

    performance = PerformanceMetrics(
        runtime=2.43,
        memory_usage=512.0,
        cpu_usage=85.0,
        iterations=1000,
        solver_calls=5,
        scalability_score=0.92,
    )

    metrics = EvaluationMetrics(
        structural=structural,
        energy=energy,
        performance=performance,
    )

    assert metrics.structural.f1_score == (0.905)

    assert metrics.energy.energy_gap == (2.6)

    assert metrics.performance.runtime == (2.43)
