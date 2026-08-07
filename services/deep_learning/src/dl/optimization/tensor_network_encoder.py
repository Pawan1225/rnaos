"""
RNAOS tensor network encoder.
"""

from __future__ import annotations

from dl.models.optimization.tensor_network import (
    TensorNetwork,
    TensorNode,
)


class TensorNetworkEncoder:
    """
    Converts tensors into tensor networks.
    """

    def encode(
        self,
        dimensions: tuple[int, ...],
    ) -> TensorNetwork:
        """
        Create tensor network structure.
        """

        nodes = tuple(
            TensorNode(
                node_id=f"T{index}",
                dimensions=(dimension,),
                rank=1,
            )
            for index, dimension in enumerate(
                dimensions,
            )
        )

        connections = tuple(
            (
                nodes[index].node_id,
                nodes[index + 1].node_id,
            )
            for index in range(
                len(nodes) - 1,
            )
        )

        return TensorNetwork(
            nodes=nodes,
            connections=connections,
        )
