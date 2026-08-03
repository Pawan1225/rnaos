import math

from optimization.models.optimization_problem import QUBOProblem
from solver.classical.simulated_annealing import (
    SimulatedAnnealingSolver,
)


def make_problem(size: int) -> QUBOProblem:
    """Create a simple QUBO problem."""

    matrix = [[-1.0 if i == j else 0.0 for j in range(size)] for i in range(size)]

    return QUBOProblem(
        matrix=matrix,
        variable_names=[f"x{i}" for i in range(size)],
    )


def test_solver_returns_result() -> None:
    """Solver should return a valid result."""

    solver = SimulatedAnnealingSolver(
        max_iterations=100,
    )

    result = solver.solve(
        make_problem(10),
    )

    assert result.solver_name == "Simulated Annealing"

    assert len(result.solution) == 10

    assert result.variable_count == 10


def test_objective_is_finite() -> None:
    """Objective value should always be finite."""

    solver = SimulatedAnnealingSolver(
        max_iterations=100,
    )

    result = solver.solve(
        make_problem(8),
    )

    assert math.isfinite(result.objective_value)


def test_runtime_non_negative() -> None:
    """Runtime should never be negative."""

    solver = SimulatedAnnealingSolver(
        max_iterations=10,
    )

    result = solver.solve(
        make_problem(5),
    )

    assert result.runtime_seconds >= 0.0


def test_iterations_reported() -> None:
    """Iteration count should match configuration."""

    solver = SimulatedAnnealingSolver(
        max_iterations=250,
    )

    result = solver.solve(
        make_problem(6),
    )

    assert result.iterations == 250
