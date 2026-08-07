"""
RNAOS demo result visualization engine.
"""

from __future__ import annotations

from apps.demo.visualization.demo_report import (
    DemoReport,
)


class ResultVisualizer:
    """
    Converts DemoResult into judge-facing report.
    """

    def create_report(
        self,
        result,
    ) -> DemoReport:
        """
        Create formatted demo report.
        """

        return DemoReport(
            title="RNAOS Optimization Result",
            sequence=result.sequence,
            predicted_structure=(result.predicted_structure),
            reference_structure=(result.reference_structure),
            accuracy=result.accuracy,
            energy_gap=result.energy_gap,
            runtime=result.runtime,
            estimated_qubits=(result.estimated_qubits),
        )
