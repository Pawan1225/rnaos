from optimization.generators.qubo_generator import QUBOGenerator
from optimization.models.optimization_problem import (
    Constraint,
    DecisionVariable,
    ObjectiveFunction,
    OptimizationMetadata,
    OptimizationProblem,
    VariableType,
)


def test_generate_qubo():
    """Test generation of a QUBO representation."""

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
        ],
        objective=ObjectiveFunction(
            expression="x0 + x1",
        ),
        constraints=[
            Constraint(
                name="c1",
                expression="x0 + x1 <= 1",
            )
        ],
        metadata=OptimizationMetadata(
            solver_hint="quantum",
            complexity_score=0.8,
        ),
    )

    qubo = QUBOGenerator().generate(problem)

    assert qubo.size == 2
    assert qubo.variable_names == ["x0", "x1"]
    assert qubo.matrix[0][0] == 1.0
    assert qubo.matrix[1][1] == 1.0
