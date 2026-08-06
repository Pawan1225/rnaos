"""
RNAOS knowledge graph node model.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class GraphNode:
    """
    Immutable biological knowledge graph node.

    Represents a biological entity within the RNA
    knowledge graph.
    """

    identifier: str

    label: str

    attributes: Mapping[
        str,
        float | str,
    ]
