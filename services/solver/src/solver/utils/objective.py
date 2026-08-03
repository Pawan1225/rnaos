"""
QUBO objective evaluation utilities.
"""

from __future__ import annotations

from optimization.models.optimization_problem import QUBOProblem


class QUBOObjectiveEvaluator:
    """Evaluate QUBO objective functions."""

    @staticmethod
    def evaluate(
        problem: QUBOProblem,
        solution: list[int],
    ) -> float:
        """
        Compute the QUBO objective value.

        The objective is:

            xᵀQx

        where:
            x is the binary solution vector
            Q is the QUBO matrix
        """

        if len(solution) != problem.size:
            raise ValueError("Solution length does not match QUBO size.")

        objective = 0.0

        for i in range(problem.size):
            for j in range(problem.size):
                objective += solution[i] * problem.matrix[i][j] * solution[j]

        return objective
