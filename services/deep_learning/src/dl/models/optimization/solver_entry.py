"""
RNAOS solver intelligence entry model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class SolverEntry:
    """
    Immutable solver registry entry.
    """

    solver_name: str

    category: str

    capability_score: float

    available: bool
