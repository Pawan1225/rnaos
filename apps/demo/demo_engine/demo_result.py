"""
RNAOS demo result model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class DemoResult:
    """
    Immutable demo execution result.
    """

    sequence: str

    predicted_structure: str

    reference_structure: str

    energy_gap: float

    accuracy: float

    runtime: float

    estimated_qubits: int
