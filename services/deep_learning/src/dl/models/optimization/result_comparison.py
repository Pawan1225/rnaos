"""
RNAOS optimization result comparison model.
"""

from __future__ import annotations

from dataclasses import dataclass

from dl.models.optimization.optimization_candidate import (
    OptimizationCandidate,
)


@dataclass(
    slots=True,
    frozen=True,
)
class ResultComparison:
    """
    Immutable optimization result comparison.
    """

    candidates: tuple[
        OptimizationCandidate,
        ...,
    ]

    best_candidate: OptimizationCandidate

    comparison_metric: str
