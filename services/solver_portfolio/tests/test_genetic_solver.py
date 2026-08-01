from optimization.models.optimization_problem import (
    Constraint,
    DecisionVariable,
    ObjectiveFunction,
    OptimizationMetadata,
    OptimizationProblem,
    VariableType,
)
from solver_portfolio.genetic.genetic_solver import (
    GeneticSolver,
)


def test_genetic_solver():
    problem = OptimizationProblem(
        variables=[
            DecisionVariable(
                name=f"x{i}",
                variable_type=VariableType.BINARY,
            )
            for i in range(8)
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
            solver_hint="genetic",
            complexity_score=0.5,
        ),
    )

    solver = GeneticSolver(
        generations=20,
        population_size=20,
    )

    result = solver.solve(problem)

    assert result.success
    assert result.solver_name == "genetic"
    assert len(result.solution) == 8
    assert result.runtime_seconds >= 0.0


def test_metadata():
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
            solver_hint="genetic",
            complexity_score=0,
        ),
    )

    result = GeneticSolver().solve(problem)

    assert "population_size" in result.metadata
    assert "generations" in result.metadata
