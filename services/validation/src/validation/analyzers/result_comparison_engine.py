"""
RNAOS result comparison engine.
"""

from __future__ import annotations

from validation.models.comparison_result import (
    ComparisonResult,
)
from validation.models.rnaos_result import (
    RNAOSResult,
)
from validation.models.vienna_reference import (
    ViennaReference,
)


class ResultComparisonEngine:
    """
    Compares RNAOS results against ViennaRNA.
    """

    def compare(
        self,
        reference: ViennaReference,
        result: RNAOSResult,
    ) -> ComparisonResult:
        """
        Calculate comparison metrics.
        """

        structure_accuracy = self._structure_accuracy(
            reference.structure,
            result.structure,
        )

        energy_gap = round(
            abs(
                reference.mfe_energy - result.energy,
            ),
            6,
        )

        runtime_difference = round(
            result.runtime,
            6,
        )

        qubit_difference = result.qubit_estimate - reference.length

        overall_score = round(
            structure_accuracy / (1.0 + energy_gap),
            6,
        )

        return ComparisonResult(
            sequence=reference.sequence,
            structure_accuracy=structure_accuracy,
            energy_gap=energy_gap,
            runtime_difference=runtime_difference,
            qubit_difference=qubit_difference,
            overall_score=overall_score,
        )

    def _structure_accuracy(
        self,
        reference: str,
        predicted: str,
    ) -> float:
        """
        Calculate dot-bracket similarity.
        """

        if not reference:
            return 0.0

        matches = sum(
            1
            for ref, pred in zip(
                reference,
                predicted,
                strict=False,
            )
            if ref == pred
        )

        return round(
            matches / len(reference),
            6,
        )
