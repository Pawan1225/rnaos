"""
RNAOS global optimization result model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class GlobalOptimizationResult:
    """
    Immutable global optimization result.
    """

    execution_id: int

    selected_solver: str

    strategy: str

    status: str
