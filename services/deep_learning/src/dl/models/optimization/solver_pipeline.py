"""
RNAOS solver pipeline model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class SolverPipeline:
    """
    Immutable hybrid solver pipeline.
    """

    pipeline_id: int

    solvers: tuple[str, ...]

    stages: int
