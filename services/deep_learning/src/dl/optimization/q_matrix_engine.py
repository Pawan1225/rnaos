"""
RNAOS Q matrix construction engine.
"""

from __future__ import annotations

from dl.models.optimization.q_matrix import (
    QMatrix,
)


class QMatrixConstructionEngine:
    """
    Builds QUBO interaction matrices.
    """

    def create(
        self,
        variables: tuple[str, ...],
        diagonal_terms: tuple[float, ...],
    ) -> QMatrix:
        """
        Create Q matrix from energy terms.
        """

        if len(variables) != len(
            diagonal_terms,
        ):
            raise ValueError(
                "Variable and term size mismatch",
            )

        size = len(
            variables,
        )

        matrix = []

        for index in range(size):
            row = [0.0 for _ in range(size)]

            row[index] = diagonal_terms[index]

            matrix.append(
                tuple(row),
            )

        return QMatrix(
            variables=variables,
            values=tuple(matrix),
        )
