"""
RNAOS knowledge graph builder utilities.
"""

from __future__ import annotations

from ai.models.graph_edge import (
    GraphEdge,
)
from ai.models.graph_node import (
    GraphNode,
)
from ai.models.knowledge_graph import (
    KnowledgeGraph,
)


class GraphBuilder:
    """
    Builder for immutable biological knowledge graphs.
    """

    def __init__(
        self,
    ) -> None:
        self._nodes: dict[
            str,
            GraphNode,
        ] = {}

        self._edges: list[GraphEdge,] = []

    def add_node(
        self,
        node: GraphNode,
    ) -> None:
        """
        Add a graph node.

        Existing nodes with the same identifier
        are ignored.
        """
        self._nodes.setdefault(
            node.identifier,
            node,
        )

    def add_edge(
        self,
        edge: GraphEdge,
    ) -> None:
        """
        Add a graph edge.
        """
        if edge.source not in self._nodes:
            raise ValueError(f"Unknown node: {edge.source}")

        if edge.target not in self._nodes:
            raise ValueError(f"Unknown node: {edge.target}")

        if edge not in self._edges:
            self._edges.append(
                edge,
            )

    def build(
        self,
    ) -> KnowledgeGraph:
        """
        Build an immutable knowledge graph.
        """
        return KnowledgeGraph(
            nodes=tuple(
                self._nodes.values(),
            ),
            edges=tuple(
                self._edges,
            ),
        )

    @property
    def node_count(
        self,
    ) -> int:
        """
        Current number of nodes.
        """
        return len(
            self._nodes,
        )

    @property
    def edge_count(
        self,
    ) -> int:
        """
        Current number of edges.
        """
        return len(
            self._edges,
        )

    def clear(
        self,
    ) -> None:
        """
        Remove all nodes and edges.
        """
        self._nodes.clear()
        self._edges.clear()
