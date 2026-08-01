from optimization.models.optimization_problem import (
    Constraint,
    DecisionVariable,
    ObjectiveFunction,
    OptimizationMetadata,
    OptimizationProblem,
    VariableType,
)
from solver_portfolio.greedy.greedy_solver import (
    GreedySolver,
)


def test_greedy_solver():
    problem = OptimizationProblem(
        variables=[
            DecisionVariable(
                name="x0",
                variable_type=VariableType.BINARY,
            ),
            DecisionVariable(
                name="x1",
                variable_type=VariableType.BINARY,
            ),
            DecisionVariable(
                name="x2",
                variable_type=VariableType.BINARY,
            ),
        ],
        objective=ObjectiveFunction(
            expression="maximize",
        ),
        constraints=[
            Constraint(
                name="dummy",
                expression="x0 <= 1",
            )
        ],
        metadata=OptimizationMetadata(
            solver_hint="greedy",
            complexity_score=0.2,
        ),
    )

    solver = GreedySolver()

    result = solver.solve(problem)

    assert result.success
    assert result.solver_name == "greedy"
    assert len(result.solution) == 3
    assert all(value == 1.0 for value in result.solution.values())


def test_runtime_is_recorded():
    problem = OptimizationProblem(
        variables=[
            DecisionVariable(
                name="x0",
                variable_type=VariableType.BINARY,
            ),
        ],
        objective=ObjectiveFunction(
            expression="maximize",
        ),
        constraints=[],
        metadata=OptimizationMetadata(
            solver_hint="greedy",
            complexity_score=0.0,
        ),
    )

    result = GreedySolver().solve(problem)

    assert result.runtime_seconds >= 0.0
