"""
RNAOS solver registry model.
"""

from __future__ import annotations

from dataclasses import dataclass

from dl.models.optimization.solver_entry import (
    SolverEntry,
)


@dataclass(
    slots=True,
    frozen=True,
)
class SolverRegistry:
    """
    Immutable solver registry.
    """

    solvers: tuple[
        SolverEntry,
        ...,
    ]

    total_solvers: int
