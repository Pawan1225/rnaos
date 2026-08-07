"""
RNAOS validation summary model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class ValidationSummary:
    """
    Immutable validation execution summary.
    """

    total_experiments: int

    successful_experiments: int

    average_energy_gap: float

    average_accuracy: float

    version: str
