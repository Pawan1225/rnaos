"""
RNAOS benchmark comparison model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    frozen=True,
    slots=True,
)
class ComparisonResult:
    """
    RNAOS versus reference comparison.
    """

    sequence: str

    structure_accuracy: float

    energy_gap: float

    rnaos_runtime: float

    reference_runtime: float

    status: str
