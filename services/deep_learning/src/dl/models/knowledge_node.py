"""
RNAOS knowledge graph node model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class KnowledgeNode:
    """
    Immutable knowledge graph node.
    """

    node_id: str

    node_type: str

    value: str
