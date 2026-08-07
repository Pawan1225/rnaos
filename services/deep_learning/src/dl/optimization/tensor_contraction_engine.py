"""
RNAOS tensor contraction engine.
"""

from __future__ import annotations

from dl.models.optimization.tensor_contraction import (
    TensorContractionResult,
)


class TensorContractionEngine:
    """
    Performs simplified tensor contractions.
    """

    def contract(
        self,
        left: tuple[float, ...],
        right: tuple[float, ...],
    ) -> TensorContractionResult:
        """
        Contract two tensor representations.
        """

        if len(left) != len(right):
            raise ValueError(
                "Tensor dimensions must match",
            )

        values = tuple(
            a * b
            for a, b in zip(
                left,
                right,
                strict=True,
            )
        )

        return TensorContractionResult(
            left_size=len(left),
            right_size=len(right),
            output_size=len(values),
            values=values,
        )
