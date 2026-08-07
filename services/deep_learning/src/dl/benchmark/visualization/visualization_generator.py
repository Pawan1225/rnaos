"""
RNAOS visualization generator.
"""

from __future__ import annotations

from dl.benchmark.visualization.accuracy_visualizer import (
    AccuracyVisualizer,
)
from dl.benchmark.visualization.energy_visualizer import (
    EnergyVisualizer,
)
from dl.benchmark.visualization.performance_visualizer import (
    PerformanceVisualizer,
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
from dl.models.benchmark.visualization_report import (
    VisualizationReport,
)


class VisualizationGenerator:
    """
    Generates benchmark visualization reports.
    """

    def __init__(self) -> None:
        self._performance = PerformanceVisualizer()

        self._accuracy = AccuracyVisualizer()

        self._energy = EnergyVisualizer()

    def generate(
        self,
        performance_metrics: tuple[
            PerformanceMetrics,
            ...,
        ],
        structural_metrics: tuple[
            StructuralMetrics,
            ...,
        ],
        energy_metrics: tuple[
            EnergyMetrics,
            ...,
        ],
    ) -> VisualizationReport:
        """
        Generate visualization report.
        """

        plots = (
            self._performance.create_runtime_plot(
                performance_metrics,
            ),
            self._accuracy.create_accuracy_plot(
                structural_metrics,
            ),
            self._energy.create_energy_plot(
                energy_metrics,
            ),
        )

        return VisualizationReport(
            report_id="VIS_REPORT_001",
            experiment_id="EXP_001",
            figures=tuple(plot.plot_id for plot in plots),
            formats=(
                "PNG",
                "PDF",
            ),
            metadata=("generator=14.7.7",),
        )
