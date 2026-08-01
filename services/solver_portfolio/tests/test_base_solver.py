from optimization.models.optimization_problem import (
    ObjectiveFunction,
    OptimizationMetadata,
    OptimizationProblem,
)
from solver_portfolio.base.base_solver import (
    BaseSolver,
    SolverResult,
)


class DummySolver(BaseSolver):
    name = "dummy"

    def solve(
        self,
        problem,
    ):
        return SolverResult(
            solver_name=self.name,
            objective_value=0.0,
            solution={},
            runtime_seconds=0.0,
            success=True,
        )


def test_dummy_solver():
    problem = OptimizationProblem(
        variables=[],
        objective=ObjectiveFunction(
            expression="0",
        ),
        constraints=[],
        metadata=OptimizationMetadata(
            solver_hint="dummy",
            complexity_score=0.0,
        ),
    )

    solver = DummySolver()

    result = solver.solve(problem)

    assert result.success
    assert result.solver_name == "dummy"
