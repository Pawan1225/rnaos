"""
QUBO Generator

Converts an OptimizationProblem into a QUBO representation.
"""

from __future__ import annotations

from optimization.models.optimization_problem import (
    OptimizationProblem,
    QUBOProblem,
)


class QUBOGenerator:
    """Generates a QUBO representation."""

    def generate(self, problem: OptimizationProblem) -> QUBOProblem:
        """
        Generate a QUBO matrix.

        Version 1:
            Identity matrix placeholder.

        Future versions:
            - Encode objective coefficients
            - Encode constraints as penalties
            - Automatic penalty scaling
        """

        size = problem.variable_count

        matrix = [[0.0 for _ in range(size)] for _ in range(size)]

        for i in range(size):
            matrix[i][i] = 1.0

        variables = [variable.name for variable in problem.variables]

        return QUBOProblem(
            matrix=matrix,
            variable_names=variables,
        )
