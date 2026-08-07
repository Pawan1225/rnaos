"""
RNAOS parallel coordination result model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class ParallelCoordinationResult:
    """
    Immutable parallel coordination result.
    """

    total_tasks: int

    completed_tasks: int

    executed_solvers: tuple[str, ...]

    success: bool
