"""
RNAOS solver intelligence entry model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class SolverIntelligenceEntry:
    """
    Immutable solver intelligence entry.
    """

    solver_name: str

    category: str

    capability_score: float

    enabled: bool
