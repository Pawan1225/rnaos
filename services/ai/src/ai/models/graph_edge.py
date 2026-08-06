"""
RNAOS knowledge graph edge model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class GraphEdge:
    """
    Immutable relationship between two biological entities.

    Each edge connects two nodes within the RNA knowledge
    graph through a semantic relationship.
    """

    source: str

    target: str

    relationship: str
