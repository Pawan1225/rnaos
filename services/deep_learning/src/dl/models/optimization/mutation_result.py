"""
RNAOS mutation result model.
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
class MutationResult:
    """
    Immutable mutation output.
    """

    original_id: int

    mutated_genome: Genome

    mutations: int
