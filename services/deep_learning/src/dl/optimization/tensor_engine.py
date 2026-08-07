"""
RNAOS tensor optimization engine.
"""

from __future__ import annotations

from dl.models.optimization.tensor_state import (
    TensorOptimizationState,
)


class TensorOptimizationEngine:
    """
    Creates tensor optimization states.
    """

    def create(
        self,
        values: tuple[float, ...],
        shape: tuple[int, ...],
    ) -> TensorOptimizationState:
        """
        Create tensor representation.
        """

        size = 1

        for dimension in shape:
            size *= dimension

        if size != len(values):
            raise ValueError(
                "Tensor shape does not match values",
            )

        return TensorOptimizationState(
            shape=shape,
            values=values,
            dimension=len(shape),
        )
