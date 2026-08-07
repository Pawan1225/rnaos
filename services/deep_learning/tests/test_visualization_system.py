"""
Tests for visualization system.
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


def test_complete_visualization_pipeline() -> None:
    """
    Complete visualization pipeline works.
    """

    generator = VisualizationGenerator()

    report = generator.generate(
        performance_metrics=(
            PerformanceMetrics(
                runtime=1.5,
                memory_usage=256.0,
                cpu_usage=75.0,
                iterations=500,
                solver_calls=3,
                scalability_score=0.92,
            ),
        ),
        structural_metrics=(
            StructuralMetrics(
                base_pair_accuracy=0.96,
                sensitivity=0.95,
                specificity=0.97,
                precision=0.94,
                recall=0.95,
                f1_score=0.945,
            ),
        ),
        energy_metrics=(
            EnergyMetrics(
                reference_energy=-30.0,
                predicted_energy=-34.0,
                energy_gap=4.0,
                relative_error=0.13,
                improvement=0.13,
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

    assert "PNG" in report.formats

    assert "PDF" in report.formats


def test_visualization_metadata() -> None:
    """
    Visualization provenance exists.
    """

    generator = VisualizationGenerator()

    report = generator.generate(
        (),
        (),
        (),
    )

    assert "generator=14.7.7" in report.metadata
