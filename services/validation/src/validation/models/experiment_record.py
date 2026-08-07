"""
RNAOS validation experiment record.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class ExperimentRecord:
    """
    Immutable scientific experiment result.
    """

    experiment_id: str

    timestamp: str

    rna_sequence: str

    sequence_length: int

    vienna_structure: str

    vienna_energy: float

    rnaos_structure: str

    rnaos_energy: float

    energy_gap: float

    accuracy: float

    runtime: float

    solver: str

    qubit_estimate: int

    variable_count: int

    iterations: int

    random_seed: int

    configuration: tuple[str, ...]
