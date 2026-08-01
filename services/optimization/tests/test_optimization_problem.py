from optimization.models.optimization_problem import (
    Constraint,
    DecisionVariable,
    ObjectiveFunction,
    OptimizationMetadata,
    OptimizationProblem,
    VariableType,
)


def test_problem_model():
    problem = OptimizationProblem(
        variables=[
            DecisionVariable(
                name="x0",
                variable_type=VariableType.BINARY,
            )
        ],
        objective=ObjectiveFunction(
            expression="x0",
        ),
        constraints=[
            Constraint(
                name="c1",
                expression="x0 <= 1",
            )
        ],
        metadata=OptimizationMetadata(
            solver_hint="classical",
            complexity_score=0.42,
        ),
    )

    assert problem.variable_count == 1

    assert problem.constraint_count == 1

    assert problem.metadata.solver_hint == "classical"
