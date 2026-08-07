"""
Tests for benchmark result.
"""

from __future__ import annotations

from dl.models.benchmark.adapter_result import (
    BenchmarkAdapterResult,
)
from dl.models.benchmark.benchmark_result import (
    BenchmarkResult,
)
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


def test_benchmark_result() -> None:
    """
    Benchmark result can be created.
    """

    adapter_result = BenchmarkAdapterResult(
        method_name="rnaos_hybrid",
        sequence="AUGCUA",
        structure="(((...)))",
        energy=-35.0,
        runtime=1.2,
        memory=256.0,
        metadata=("version=14.6",),
    )

    metrics = EvaluationMetrics(
        structural=StructuralMetrics(
            base_pair_accuracy=0.95,
            sensitivity=0.94,
            specificity=0.96,
            precision=0.93,
            recall=0.94,
            f1_score=0.935,
        ),
        energy=EnergyMetrics(
            reference_energy=-32.5,
            predicted_energy=-35.0,
            energy_gap=2.5,
            relative_error=0.07,
            improvement=0.07,
        ),
        performance=PerformanceMetrics(
            runtime=1.2,
            memory_usage=256.0,
            cpu_usage=70.0,
            iterations=500,
            solver_calls=3,
            scalability_score=0.9,
        ),
    )

    result = BenchmarkResult(
        case_id="CASE_001",
        method_name="rnaos_hybrid",
        adapter_result=adapter_result,
        evaluation_metrics=metrics,
        success=True,
        metadata=("seed=42",),
    )

    assert result.case_id == ("CASE_001")

    assert result.method_name == ("rnaos_hybrid")

    assert result.success is True

    assert result.adapter_result.energy == -35.0
