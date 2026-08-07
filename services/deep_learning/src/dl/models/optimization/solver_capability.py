"""
RNAOS solver capability model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class SolverCapability:
    """
    Immutable solver capability representation.
    """

    solver_name: str

    capabilities: tuple[float, ...]

    category: str
