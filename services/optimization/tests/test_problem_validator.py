from optimization.models.optimization_problem import (
    Constraint,
    DecisionVariable,
    ObjectiveFunction,
    OptimizationMetadata,
    OptimizationProblem,
    VariableType,
)
from optimization.validators.problem_validator import (
    OptimizationProblemValidator,
)


def test_valid_problem():
    """Test validation of a valid optimization problem."""

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
            complexity_score=0.5,
        ),
    )

    result = OptimizationProblemValidator().validate(problem)

    assert result.is_valid
    assert result.errors == []


def test_duplicate_variable_names():
    """Duplicate variable names should fail validation."""

    problem = OptimizationProblem(
        variables=[
            DecisionVariable(
                name="x0",
                variable_type=VariableType.BINARY,
            ),
            DecisionVariable(
                name="x0",
                variable_type=VariableType.BINARY,
            ),
        ],
        objective=ObjectiveFunction(
            expression="x0",
        ),
        constraints=[],
        metadata=OptimizationMetadata(
            solver_hint="classical",
            complexity_score=0.5,
        ),
    )

    result = OptimizationProblemValidator().validate(problem)

    assert not result.is_valid
    assert any("Duplicate variable names" in error for error in result.errors)


def test_empty_objective():
    """Empty objectives should fail validation."""

    problem = OptimizationProblem(
        variables=[
            DecisionVariable(
                name="x0",
                variable_type=VariableType.BINARY,
            )
        ],
        objective=ObjectiveFunction(
            expression="",
        ),
        constraints=[],
        metadata=OptimizationMetadata(
            solver_hint="classical",
            complexity_score=0.5,
        ),
    )

    result = OptimizationProblemValidator().validate(problem)

    assert not result.is_valid
