"""
RNAOS knowledge graph engine.
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
from ai.utils.graph_builder import (
    GraphBuilder,
)
from biology.models.biological_intelligence_profile import (
    BiologicalIntelligenceProfile,
)


class KnowledgeGraphEngine:
    """
    Generate deterministic biological knowledge graphs.

    Architecture
    ------------
    Converts a biological intelligence profile into
    an immutable semantic graph representation.

    Complexity
    ----------
    Time Complexity: O(1)

    The engine creates a fixed number of biological
    entities and relationships.
    """

    def __init__(
        self,
        builder: GraphBuilder | None = None,
    ) -> None:
        """
        Initialize the knowledge graph engine.

        Parameters
        ----------
        builder
            Optional graph builder for dependency injection.
        """
        self._builder = builder or GraphBuilder()

    def _add_nodes(
        self,
        builder: GraphBuilder,
        profile: BiologicalIntelligenceProfile,
    ) -> None:
        """
        Add biological entities.
        """
        builder.add_node(
            GraphNode(
                identifier="sequence",
                label="RNA Sequence",
                attributes={
                    "length": float(
                        profile.sequence.length,
                    ),
                },
            )
        )

        builder.add_node(
            GraphNode(
                identifier="gc_content",
                label="GC Content",
                attributes={
                    "gc_content": profile.gc_content.gc_content,
                    "au_content": profile.gc_content.au_content,
                },
            )
        )

        builder.add_node(
            GraphNode(
                identifier="complexity",
                label="Complexity",
                attributes={
                    "score": profile.complexity.complexity_score,
                },
            )
        )

        builder.add_node(
            GraphNode(
                identifier="motifs",
                label="Motifs",
                attributes={
                    "count": float(
                        len(profile.motifs.canonical),
                    ),
                },
            )
        )

        builder.add_node(
            GraphNode(
                identifier="stem_loops",
                label="Stem Loops",
                attributes={
                    "count": float(
                        profile.stem_loops.estimated_stems,
                    ),
                },
            )
        )

        builder.add_node(
            GraphNode(
                identifier="thermodynamics",
                label="Thermodynamics",
                attributes={
                    "stability": (profile.thermodynamics.stability_index),
                },
            )
        )

    def _add_edges(
        self,
        builder: GraphBuilder,
    ) -> None:
        """
        Add biological relationships.
        """
        relationships = (
            (
                "sequence",
                "gc_content",
                "HAS_GC_CONTENT",
            ),
            (
                "sequence",
                "complexity",
                "HAS_COMPLEXITY",
            ),
            (
                "sequence",
                "motifs",
                "HAS_MOTIFS",
            ),
            (
                "sequence",
                "stem_loops",
                "HAS_STEM_LOOPS",
            ),
            (
                "sequence",
                "thermodynamics",
                "HAS_THERMODYNAMICS",
            ),
        )

        for source, target, relation in relationships:
            builder.add_edge(
                GraphEdge(
                    source=source,
                    target=target,
                    relationship=relation,
                )
            )

    def build(
        self,
        profile: BiologicalIntelligenceProfile,
    ) -> KnowledgeGraph:
        """
        Generate a biological knowledge graph.
        """
        self._builder.clear()

        self._add_nodes(
            self._builder,
            profile,
        )

        self._add_edges(
            self._builder,
        )

        return self._builder.build()
