"""
RNAOS QUBO construction engine.
"""

from __future__ import annotations

from dl.models.optimization.qubo_model import (
    QUBOModel,
)


class QUBOEngine:
    """
    Builds QUBO optimization models.
    """

    def create(
        self,
        variables: tuple[str, ...],
        matrix: tuple[
            tuple[float, ...],
            ...,
        ],
        offset: float = 0.0,
    ) -> QUBOModel:
        """
        Create QUBO model.
        """

        size = len(
            variables,
        )

        if len(matrix) != size:
            raise ValueError(
                "QUBO matrix size mismatch",
            )

        for row in matrix:
            if len(row) != size:
                raise ValueError(
                    "QUBO matrix must be square",
                )

        return QUBOModel(
            variables=variables,
            matrix=matrix,
            offset=offset,
        )
