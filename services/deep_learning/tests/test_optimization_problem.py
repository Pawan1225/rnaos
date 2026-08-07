"""
Tests for optimization problem model.
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
from dl.optimization.problem_builder import (
    OptimizationProblemBuilder,
)


def test_create_problem() -> None:
    """
    Optimization problem is created.
    """

    builder = OptimizationProblemBuilder()

    problem = builder.build(
        name="rna_folding",
        variables=(
            OptimizationVariable(
                variable_id="x1",
                index=0,
            ),
        ),
        constraints=(
            Constraint(
                name="valid_pairing",
                penalty=10.0,
            ),
        ),
        objective="minimize_energy",
    )

    assert isinstance(
        problem,
        OptimizationProblem,
    )

    assert problem.name == "rna_folding"


def test_problem_components() -> None:
    """
    Problem stores components.
    """

    builder = OptimizationProblemBuilder()

    problem = builder.build(
        name="test",
        variables=(),
        constraints=(),
        objective="energy",
    )

    assert problem.variables == ()

    assert problem.constraints == ()
