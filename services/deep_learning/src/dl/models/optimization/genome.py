"""
RNAOS genetic genome model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class Genome:
    """
    Immutable genetic representation.
    """

    genome_id: int

    sequence: tuple[int, ...]

    fitness: float

    generation: int
