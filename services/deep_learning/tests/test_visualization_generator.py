"""
Tests for visualization generator.
"""

from __future__ import annotations

from dl.benchmark.visualization.visualization_generator import (
    VisualizationGenerator,
)
from dl.models.benchmark.energy_metrics import (
    EnergyMetrics,
)
from dl.models.benchmark.performance_metrics import (
    PerformanceMetrics,
)
from dl.models.benchmark.structural_metrics import (
    StructuralMetrics,
)


def test_visualization_generator() -> None:
    """
    Generator creates visualization report.
    """

    generator = VisualizationGenerator()

    report = generator.generate(
        performance_metrics=(
            PerformanceMetrics(
                runtime=2.0,
                memory_usage=512.0,
                cpu_usage=80.0,
                iterations=100,
                solver_calls=2,
                scalability_score=0.9,
            ),
        ),
        structural_metrics=(
            StructuralMetrics(
                base_pair_accuracy=0.95,
                sensitivity=0.94,
                specificity=0.96,
                precision=0.93,
                recall=0.94,
                f1_score=0.935,
            ),
        ),
        energy_metrics=(
            EnergyMetrics(
                reference_energy=-32.5,
                predicted_energy=-35.0,
                energy_gap=2.5,
                relative_error=0.07,
                improvement=0.07,
            ),
        ),
    )

    assert report.report_id == ("VIS_REPORT_001")

    assert (
        len(
            report.figures,
        )
        == 3
    )
