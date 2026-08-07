"""
RNAOS energy evaluation metrics model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class EnergyMetrics:
    """
    Immutable RNA energy comparison metrics.
    """

    reference_energy: float

    predicted_energy: float

    energy_gap: float

    relative_error: float

    improvement: float
