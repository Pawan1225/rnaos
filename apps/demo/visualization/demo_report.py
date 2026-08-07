"""
RNAOS demo visualization report model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    frozen=True,
    slots=True,
)
class DemoReport:
    """
    Human-readable RNAOS demo report.
    """

    title: str

    sequence: str

    predicted_structure: str

    reference_structure: str

    accuracy: float

    energy_gap: float

    runtime: float

    estimated_qubits: int
