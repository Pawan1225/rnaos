"""
RNAOS solver combination rule model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class SolverCombinationRule:
    """
    Immutable solver combination rule.
    """

    primary_solver: str
    secondary_solver: str
    refinement_solver: str
    condition: str
