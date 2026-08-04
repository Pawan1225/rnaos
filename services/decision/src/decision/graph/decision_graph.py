"""
Decision reasoning graph.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from decision.models.explanation import Explanation


@dataclass(slots=True)
class DecisionNode:
    """Node in the reasoning graph."""

    identifier: str

    explanation: Explanation

    metadata: dict[str, object] = field(
        default_factory=dict,
    )


@dataclass(slots=True)
class DecisionEdge:
    """Directed relationship between two decision nodes."""

    source: str

    target: str

    relationship: str


class DecisionGraph:
    """Graph representing the complete decision-making process."""

    def __init__(self) -> None:
        self.nodes: dict[str, DecisionNode] = {}

        self.edges: list[DecisionEdge] = []

    def add_node(
        self,
        node: DecisionNode,
    ) -> None:
        """Add or replace a decision node."""

        self.nodes[node.identifier] = node

    def add_edge(
        self,
        source: str,
        target: str,
        relationship: str,
    ) -> None:
        """Create a directed relationship."""

        self.edges.append(
            DecisionEdge(
                source=source,
                target=target,
                relationship=relationship,
            )
        )

    def children(
        self,
        identifier: str,
    ) -> list[str]:
        """Return all child node identifiers."""

        return [edge.target for edge in self.edges if edge.source == identifier]

    def parents(
        self,
        identifier: str,
    ) -> list[str]:
        """Return all parent node identifiers."""

        return [edge.source for edge in self.edges if edge.target == identifier]

    def has_node(
        self,
        identifier: str,
    ) -> bool:
        """Return whether a node exists."""

        return identifier in self.nodes

    def node(
        self,
        identifier: str,
    ) -> DecisionNode:
        """Return a decision node."""

        return self.nodes[identifier]
