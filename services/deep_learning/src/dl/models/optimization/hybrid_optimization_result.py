"""
RNAOS hybrid optimization result model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class HybridOptimizationResult:
    """
    Immutable hybrid optimization result.
    """

    strategy_name: str

    executed_solvers: tuple[str, ...]

    status: str

    best_solver: str

    confidence: float
