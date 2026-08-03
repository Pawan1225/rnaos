from math import isfinite

from optimization.models.optimization_problem import QUBOProblem
from solver.classical.exact_solver import ExactSolver


def make_problem(size: int) -> QUBOProblem:
    """Create a simple diagonal QUBO problem."""

    matrix = [[0.0 for _ in range(size)] for _ in range(size)]

    for i in range(size):
        matrix[i][i] = -1.0

    return QUBOProblem(
        matrix=matrix,
        variable_names=[f"x{i}" for i in range(size)],
    )


def test_solver_returns_result() -> None:
    """Solver should return a valid result."""

    problem = make_problem(4)

    result = ExactSolver().solve(problem)

    assert result.solver_name == "Exact Solver"


def test_solution_length() -> None:
    """Solution length should match problem size."""

    problem = make_problem(5)

    result = ExactSolver().solve(problem)

    assert len(result.solution) == 5


def test_solution_binary() -> None:
    """Solution should contain only binary values."""

    problem = make_problem(6)

    result = ExactSolver().solve(problem)

    assert all(bit in (0, 1) for bit in result.solution)


def test_objective_finite() -> None:
    """Objective value should be finite."""

    problem = make_problem(5)

    result = ExactSolver().solve(problem)

    assert isfinite(result.objective_value)


def test_runtime_non_negative() -> None:
    """Runtime should never be negative."""

    problem = make_problem(5)

    result = ExactSolver().solve(problem)

    assert result.runtime_seconds >= 0.0


def test_evaluation_count() -> None:
    """Exact solver should evaluate all binary assignments."""

    problem = make_problem(4)

    result = ExactSolver().solve(problem)

    assert result.metadata["evaluations"] == 2**4

    assert result.iterations == 2**4
