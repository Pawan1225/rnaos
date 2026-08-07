"""
Tests for RNA folding graph engine.
"""

from __future__ import annotations

from dl.models.optimization.rna_graph import (
    RNAInteractionEdge,
    RNANode,
)
from dl.optimization.rna_graph_engine import (
    RNAFoldingGraphEngine,
)


def test_build_rna_nodes() -> None:
    """
    RNA sequence creates graph nodes.
    """

    engine = RNAFoldingGraphEngine()

    nodes = engine.build_nodes(
        "AUGC",
    )

    assert nodes == (
        RNANode(
            index=0,
            nucleotide="A",
        ),
        RNANode(
            index=1,
            nucleotide="U",
        ),
        RNANode(
            index=2,
            nucleotide="G",
        ),
        RNANode(
            index=3,
            nucleotide="C",
        ),
    )


def test_create_interaction_edge() -> None:
    """
    RNA interaction edges are created.
    """

    engine = RNAFoldingGraphEngine()

    edge = engine.add_interaction(
        source=0,
        target=1,
        interaction_type="AU",
        energy=-2.0,
    )

    assert edge == RNAInteractionEdge(
        source=0,
        target=1,
        interaction_type="AU",
        energy=-2.0,
    )
