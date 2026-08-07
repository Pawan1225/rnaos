"""
RNAOS optimization penalty models.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class PenaltyConfiguration:
    """
    Immutable optimization penalty configuration.
    """

    constraint_name: str

    penalty_value: float
