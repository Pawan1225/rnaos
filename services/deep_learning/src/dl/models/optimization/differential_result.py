"""
RNAOS differential evolution result model.
"""

from __future__ import annotations

from dataclasses import dataclass

from dl.models.optimization.differential_vector import (
    DifferentialVector,
)


@dataclass(
    slots=True,
    frozen=True,
)
class DifferentialResult:
    """
    Immutable differential evolution result.
    """

    best_vector: DifferentialVector

    generations: int

    converged: bool
