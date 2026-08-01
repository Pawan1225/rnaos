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
from solver_portfolio.genetic.genetic_solver import (
    GeneticSolver,
)
from solver_portfolio.greedy.greedy_solver import (
    GreedySolver,
)


def create_problem():
    return OptimizationProblem(
        variables=[
            DecisionVariable(
                name=f"x{i}",
                variable_type=VariableType.BINARY,
            )
            for i in range(10)
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
            complexity_score=0.5,
        ),
    )


def test_all_solvers():
    problem = create_problem()

    solvers = [
        GreedySolver(),
        SimulatedAnnealingSolver(
            iterations=20,
        ),
        GeneticSolver(
            generations=20,
        ),
    ]

    for solver in solvers:
        result = solver.solve(problem)

        assert result.success
        assert len(result.solution) == 10
