from optimization.models.optimization_problem import (
    Constraint,
    DecisionVariable,
    ObjectiveFunction,
    OptimizationMetadata,
    OptimizationProblem,
    VariableType,
)
from solver_portfolio.annealing.simulated_annealing_solver import (
    SimulatedAnnealingSolver,
)


def test_sa_solver():
    problem = OptimizationProblem(
        variables=[
            DecisionVariable(
                name=f"x{i}",
                variable_type=VariableType.BINARY,
            )
            for i in range(5)
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
            solver_hint="annealing",
            complexity_score=0.5,
        ),
    )

    solver = SimulatedAnnealingSolver(
        iterations=50,
    )

    result = solver.solve(problem)

    assert result.success

    assert result.solver_name == "simulated_annealing"

    assert len(result.solution) == 5

    assert result.runtime_seconds >= 0.0


def test_sa_metadata():
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
            solver_hint="annealing",
            complexity_score=0.0,
        ),
    )

    result = SimulatedAnnealingSolver().solve(problem)

    assert "iterations" in result.metadata

    assert "temperature" in result.metadata
