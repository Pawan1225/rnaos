"""
Experiment result serializer.

Converts ExperimentResult models
into scientific artifact records.
"""

from __future__ import annotations

from validation.models.experiment_result import (
    ExperimentResult,
)


class ExperimentResultSerializer:
    """
    Serializes experiment results.
    """

    def serialize(
        self,
        result: ExperimentResult,
    ) -> dict:
        """
        Convert ExperimentResult to dict.
        """

        return {
            "experiment_id": (result.experiment_id),
            "sequence_id": (result.sequence_id),
            "sequence": (result.sequence),
            "sequence_length": (result.sequence_length),
            "rnaos_structure": (result.rnaos_structure),
            "reference_structure": (result.reference_structure),
            "rnaos_energy": (result.rnaos_energy),
            "reference_energy": (result.reference_energy),
            "energy_gap": (result.energy_gap),
            "accuracy": (result.accuracy),
            "runtime_seconds": (result.runtime_seconds),
            "estimated_qubits": (result.estimated_qubits),
        }
