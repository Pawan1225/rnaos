"""
RNAOS crossover result model.
"""

from __future__ import annotations

from dataclasses import dataclass

from dl.models.optimization.genome import (
    Genome,
)


@dataclass(
    slots=True,
    frozen=True,
)
class CrossoverResult:
    """
    Immutable crossover output.
    """

    parent_a_id: int

    parent_b_id: int

    child: Genome

    crossover_point: int
