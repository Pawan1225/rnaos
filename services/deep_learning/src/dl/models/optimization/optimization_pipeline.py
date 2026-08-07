"""
RNAOS optimization pipeline model.
"""

from __future__ import annotations

from dataclasses import dataclass

from dl.models.optimization.optimization_stage import (
    OptimizationStage,
)


@dataclass(
    slots=True,
    frozen=True,
)
class OptimizationPipeline:
    """
    Immutable optimization pipeline.
    """

    pipeline_id: int

    name: str

    stages: tuple[OptimizationStage, ...]

    status: str
