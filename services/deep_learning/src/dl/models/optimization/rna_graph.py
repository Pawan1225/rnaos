"""
RNAOS optimization graph models.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class RNANode:
    """
    RNA nucleotide node.
    """

    index: int

    nucleotide: str


@dataclass(
    slots=True,
    frozen=True,
)
class RNAInteractionEdge:
    """
    Possible RNA interaction edge.
    """

    source: int

    target: int

    interaction_type: str

    energy: float
