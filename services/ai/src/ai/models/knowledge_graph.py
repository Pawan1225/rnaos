"""
RNAOS biological knowledge graph model.
"""

from __future__ import annotations

from dataclasses import dataclass

from ai.models.graph_edge import (
    GraphEdge,
)
from ai.models.graph_node import (
    GraphNode,
)


@dataclass(slots=True, frozen=True)
class KnowledgeGraph:
    """
    Immutable biological knowledge graph.

    Stores biological entities (nodes) and their
    semantic relationships (edges).
    """

    nodes: tuple[GraphNode, ...]

    edges: tuple[GraphEdge, ...]

    @property
    def node_count(
        self,
    ) -> int:
        """
        Return the number of graph nodes.
        """
        return len(
            self.nodes,
        )

    @property
    def edge_count(
        self,
    ) -> int:
        """
        Return the number of graph edges.
        """
        return len(
            self.edges,
        )

    @property
    def is_empty(
        self,
    ) -> bool:
        """
        Check whether the graph is empty.
        """
        return self.node_count == 0 and self.edge_count == 0

    @property
    def summary(
        self,
    ) -> str:
        """
        Human-readable graph summary.
        """
        return f"{self.node_count} nodes, {self.edge_count} edges"
