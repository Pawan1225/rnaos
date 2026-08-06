"""
Tests for the RNAOS knowledge graph engine.
"""

from __future__ import annotations

import pytest
from ai.analyzers.knowledge_graph_engine import (
    KnowledgeGraphEngine,
)
from ai.models.knowledge_graph import (
    KnowledgeGraph,
)
from biology.analyzers.biological_intelligence_engine import (
    BiologicalIntelligenceEngine,
)


@pytest.fixture
def biology_engine() -> BiologicalIntelligenceEngine:
    """Create a biological intelligence engine."""
    return BiologicalIntelligenceEngine()


@pytest.fixture
def graph_engine() -> KnowledgeGraphEngine:
    """Create a knowledge graph engine."""
    return KnowledgeGraphEngine()


@pytest.fixture
def graph(
    biology_engine: BiologicalIntelligenceEngine,
    graph_engine: KnowledgeGraphEngine,
) -> KnowledgeGraph:
    """Create a biological knowledge graph."""
    profile = biology_engine.analyze(
        "GCGAAACGC",
    )

    return graph_engine.build(
        profile,
    )


def test_graph_creation(
    graph: KnowledgeGraph,
) -> None:
    """Graph should be created successfully."""
    assert graph is not None


def test_graph_contains_nodes(
    graph: KnowledgeGraph,
) -> None:
    """Graph should contain biological nodes."""
    assert (
        len(
            graph.nodes,
        )
        > 0
    )


def test_graph_contains_edges(
    graph: KnowledgeGraph,
) -> None:
    """Graph should contain biological relationships."""
    assert (
        len(
            graph.edges,
        )
        > 0
    )


def test_graph_not_empty(
    graph: KnowledgeGraph,
) -> None:
    """Graph should contain nodes and edges."""
    assert not graph.is_empty


def test_edge_endpoints_exist(
    graph: KnowledgeGraph,
) -> None:
    """Every edge should reference existing nodes."""
    node_ids = {node.identifier for node in graph.nodes}

    for edge in graph.edges:
        assert edge.source in node_ids
        assert edge.target in node_ids


def test_sequence_node_exists(
    graph: KnowledgeGraph,
) -> None:
    """Sequence node should exist."""
    identifiers = {node.identifier for node in graph.nodes}

    assert "sequence" in identifiers


def test_gc_content_node_exists(
    graph: KnowledgeGraph,
) -> None:
    """GC content node should exist."""
    identifiers = {node.identifier for node in graph.nodes}

    assert "gc_content" in identifiers


def test_complexity_node_exists(
    graph: KnowledgeGraph,
) -> None:
    """Complexity node should exist."""
    identifiers = {node.identifier for node in graph.nodes}

    assert "complexity" in identifiers


def test_deterministic_graph_generation(
    biology_engine: BiologicalIntelligenceEngine,
    graph_engine: KnowledgeGraphEngine,
) -> None:
    """Graph generation should be deterministic."""
    profile = biology_engine.analyze(
        "GCGAAACGC",
    )

    graph1 = graph_engine.build(
        profile,
    )

    graph2 = graph_engine.build(
        profile,
    )

    assert graph1 == graph2
