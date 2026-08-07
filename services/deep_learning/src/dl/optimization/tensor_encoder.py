"""
RNAOS tensor representation encoder.
"""

from __future__ import annotations

from dl.models.optimization.tensor_representation import (
    TensorRepresentation,
)


class TensorEncoder:
    """
    Converts optimization values into tensors.
    """

    def encode(
        self,
        values: tuple[float, ...],
        dimensions: tuple[int, ...],
    ) -> TensorRepresentation:
        """
        Create tensor representation.
        """

        expected_size = 1

        for dimension in dimensions:
            expected_size *= dimension

        if expected_size != len(values):
            raise ValueError(
                "Tensor dimensions mismatch",
            )

        return TensorRepresentation(
            dimensions=dimensions,
            rank=len(
                dimensions,
            ),
            values=values,
        )
