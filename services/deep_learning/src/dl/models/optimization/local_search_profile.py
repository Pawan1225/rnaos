"""
RNAOS local search profile model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class LocalSearchProfile:
    """
    Immutable local search intelligence profile.
    """

    best_energy: float

    iterations: int

    search_strategy: str

    confidence: float
