"""
RNAOS optimization problem builder.
"""

from __future__ import annotations

from dl.models.optimization.constraint import (
    Constraint,
)
from dl.models.optimization.optimization_problem import (
    OptimizationProblem,
)
from dl.models.optimization.optimization_variable import (
    OptimizationVariable,
)


class OptimizationProblemBuilder:
    """
    Builds unified optimization problems.
    """

    def build(
        self,
        name: str,
        variables: tuple[
            OptimizationVariable,
            ...,
        ],
        constraints: tuple[
            Constraint,
            ...,
        ],
        objective: str,
    ) -> OptimizationProblem:
        """
        Create optimization problem.
        """

        return OptimizationProblem(
            name=name,
            variables=variables,
            constraints=constraints,
            objective=objective,
        )
