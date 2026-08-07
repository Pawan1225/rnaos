"""
RNAOS optimization stage model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class OptimizationStage:
    """
    Immutable optimization stage.
    """

    stage_id: int

    name: str

    solver_name: str

    priority: int

    status: str
