"""
RNAOS optimization energy models.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class EnergyResult:
    """
    Immutable optimization energy result.
    """

    energy: float

    valid: bool
