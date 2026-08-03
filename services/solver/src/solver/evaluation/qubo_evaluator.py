"""
Shared QUBO evaluator.

Provides the canonical evaluation interface used by every solver.
"""

from __future__ import annotations

from optimization.models.optimization_problem import QUBOProblem

from solver.utils import QUBOObjectiveEvaluator


class QUBOEvaluator:
    """Shared interface for QUBO evaluation."""

    @staticmethod
    def evaluate(
        problem: QUBOProblem,
        solution: list[int],
    ) -> float:
        """Evaluate the QUBO objective."""

        return QUBOObjectiveEvaluator.evaluate(
            problem,
            solution,
        )
