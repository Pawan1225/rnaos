"""
RNAOS hybrid optimization profile models.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class HybridOptimizationProfile:
    """
    Immutable hybrid optimization profile.
    """

    strategy: str

    selected_solver: str

    solvers_used: tuple[str, ...]

    final_energy: float

    confidence: float

    stages_completed: int
