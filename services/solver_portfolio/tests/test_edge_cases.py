from optimization.models.optimization_problem import (
    ObjectiveFunction,
    OptimizationMetadata,
    OptimizationProblem,
)
from solver_portfolio.greedy.greedy_solver import (
    GreedySolver,
)


def test_empty_problem():
    problem = OptimizationProblem(
        variables=[],
        objective=ObjectiveFunction(
            expression="0",
        ),
        constraints=[],
        metadata=OptimizationMetadata(
            solver_hint="greedy",
            complexity_score=0,
        ),
    )

    result = GreedySolver().solve(problem)

    assert result.success
    assert result.solution == {}
