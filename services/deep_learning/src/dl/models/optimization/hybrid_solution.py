"""
RNAOS hybrid optimization solution model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class HybridSolution:
    """
    Immutable hybrid optimization solution.
    """

    solution_id: int

    strategy_name: str

    objective_score: float

    success: bool
