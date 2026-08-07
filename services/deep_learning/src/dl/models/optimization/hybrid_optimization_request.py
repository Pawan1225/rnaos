"""
RNAOS hybrid optimization request model.
"""

from __future__ import annotations

from dataclasses import dataclass

from dl.models.optimization.optimization_pipeline import (
    OptimizationPipeline,
)


@dataclass(
    slots=True,
    frozen=True,
)
class HybridOptimizationRequest:
    """
    Immutable hybrid optimization request.
    """

    request_id: int

    problem_id: str

    pipeline: OptimizationPipeline

    target_accuracy: float

    priority: int

    status: str
