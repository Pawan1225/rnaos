"""
RNAOS comparison result model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class ComparisonResult:
    """
    Immutable RNAOS benchmark comparison.
    """

    sequence: str

    structure_accuracy: float

    energy_gap: float

    runtime_difference: float

    qubit_difference: int

    overall_score: float
