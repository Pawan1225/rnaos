"""
RNAOS optimization constraint models.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class Constraint:
    """
    Immutable optimization constraint.
    """

    name: str

    penalty: float
