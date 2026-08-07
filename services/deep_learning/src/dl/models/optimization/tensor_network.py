"""
RNAOS tensor network models.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class TensorNode:
    """
    Immutable tensor network node.
    """

    node_id: str

    dimensions: tuple[int, ...]

    rank: int


@dataclass(
    slots=True,
    frozen=True,
)
class TensorNetwork:
    """
    Immutable tensor network representation.
    """

    nodes: tuple[TensorNode, ...]

    connections: tuple[tuple[str, str], ...]
