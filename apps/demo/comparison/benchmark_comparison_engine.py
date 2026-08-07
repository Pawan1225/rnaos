"""
RNAOS benchmark comparison engine.
"""

from __future__ import annotations

from apps.demo.comparison.comparison_result import (
    ComparisonResult,
)


class BenchmarkComparisonEngine:
    """
    Compares RNAOS output against reference.
    """

    def compare(
        self,
        rnaos_result,
        reference_result,
    ) -> ComparisonResult:
        """
        Generate comparison metrics.
        """

        accuracy = 1.0 if (rnaos_result.predicted_structure == reference_result.structure) else 0.0

        return ComparisonResult(
            sequence=rnaos_result.sequence,
            structure_accuracy=accuracy,
            energy_gap=(rnaos_result.energy_gap),
            rnaos_runtime=(rnaos_result.runtime),
            reference_runtime=(reference_result.runtime),
            status="COMPLETE",
        )
