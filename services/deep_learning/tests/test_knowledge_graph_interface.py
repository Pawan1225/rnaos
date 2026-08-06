"""
Tests for RNA knowledge graph interface.
"""

from __future__ import annotations

from dl.knowledge.knowledge_graph_interface import (
    RNAKnowledgeGraphInterface,
)
from dl.models.knowledge_node import (
    KnowledgeNode,
)


def test_add_and_retrieve_node() -> None:
    """
    Knowledge nodes can be stored.
    """

    graph = RNAKnowledgeGraphInterface()

    node = KnowledgeNode(
        node_id="rna_001",
        node_type="sequence",
        value="AUGC",
    )

    graph.add_node(
        node,
    )

    result = graph.get_node(
        "rna_001",
    )

    assert result == node


def test_list_nodes() -> None:
    """
    Graph lists stored nodes.
    """

    graph = RNAKnowledgeGraphInterface()

    graph.add_node(
        KnowledgeNode(
            node_id="structure_001",
            node_type="structure",
            value="(((...)))",
        ),
    )

    assert graph.list_nodes() == ("structure_001",)
