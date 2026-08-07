"""
RNAOS optimization variable models.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class OptimizationVariable:
    """
    Immutable optimization variable.

    Represents a decision variable
    used in optimization formulations.
    """

    variable_id: str

    index: int

    binary: bool = True


@dataclass(
    slots=True,
    frozen=True,
)
class BasePairVariable:
    """
    RNA base pairing decision variable.

    Represents whether two nucleotides
    form a pair.
    """

    variable_id: str

    nucleotide_i: int

    nucleotide_j: int

    pair_type: str

    selected: bool = False
