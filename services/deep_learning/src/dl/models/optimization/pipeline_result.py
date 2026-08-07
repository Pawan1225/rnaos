"""
RNAOS optimization pipeline result models.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class PipelineResult:
    """
    Immutable pipeline result.
    """

    selected_solver: str

    energy: float

    stages_completed: int

    confidence: float
