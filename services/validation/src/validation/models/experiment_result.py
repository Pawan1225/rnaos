"""
RNAOS benchmark experiment result model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class ExperimentResult:
    """
    Stores one benchmark experiment result.
    """

    experiment_id: int

    sequence_id: str

    sequence: str

    sequence_length: int

    rnaos_structure: str

    reference_structure: str

    rnaos_energy: float

    reference_energy: float

    energy_gap: float

    accuracy: float

    runtime_seconds: float

    estimated_qubits: int

    structure_precision: float = 0.0

    structure_recall: float = 0.0

    structure_f1: float = 0.0

    base_pair_distance: float = 0.0
