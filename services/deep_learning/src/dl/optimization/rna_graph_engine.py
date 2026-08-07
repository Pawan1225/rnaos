"""
RNAOS folding graph representation engine.
"""

from __future__ import annotations

from dl.models.optimization.rna_graph import (
    RNAInteractionEdge,
    RNANode,
)


class RNAFoldingGraphEngine:
    """
    Creates RNA optimization graphs.
    """

    def build_nodes(
        self,
        sequence: str,
    ) -> tuple[RNANode, ...]:
        """
        Convert sequence into nodes.
        """

        return tuple(
            RNANode(
                index=index,
                nucleotide=value,
            )
            for index, value in enumerate(sequence)
        )

    def add_interaction(
        self,
        source: int,
        target: int,
        interaction_type: str,
        energy: float,
    ) -> RNAInteractionEdge:
        """
        Create interaction edge.
        """

        return RNAInteractionEdge(
            source=source,
            target=target,
            interaction_type=interaction_type,
            energy=energy,
        )
