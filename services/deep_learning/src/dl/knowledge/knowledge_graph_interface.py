"""
RNAOS knowledge graph interface.
"""

from __future__ import annotations

from dl.models.knowledge_node import (
    KnowledgeNode,
)


class RNAKnowledgeGraphInterface:
    """
    Stores RNA intelligence relationships.
    """

    def __init__(
        self,
    ) -> None:
        self._nodes: dict[
            str,
            KnowledgeNode,
        ] = {}

    def add_node(
        self,
        node: KnowledgeNode,
    ) -> None:
        """
        Add knowledge node.
        """

        self._nodes[node.node_id] = node

    def get_node(
        self,
        node_id: str,
    ) -> KnowledgeNode:
        """
        Retrieve knowledge node.
        """

        return self._nodes[node_id]

    def list_nodes(
        self,
    ) -> tuple[str, ...]:
        """
        List graph nodes.
        """

        return tuple(
            self._nodes.keys(),
        )
