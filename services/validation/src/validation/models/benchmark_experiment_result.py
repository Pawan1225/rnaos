"""
RNAOS benchmark experiment result model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    frozen=True,
    slots=True,
)
class BenchmarkExperimentResult:
    """
    Single benchmark experiment record.
    """

    experiment_id: int

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
