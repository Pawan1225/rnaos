from math import isfinite

from optimization.models.optimization_problem import QUBOProblem
from solver.classical.genetic_algorithm import (
    GeneticAlgorithmSolver,
)


def make_problem(size: int) -> QUBOProblem:
    """Create a simple QUBO problem."""

    matrix = [[0.0 for _ in range(size)] for _ in range(size)]

    for i in range(size):
        matrix[i][i] = -1.0

    return QUBOProblem(
        matrix=matrix,
        variable_names=[f"x{i}" for i in range(size)],
    )


def test_solver_returns_result() -> None:
    """Solver should return a valid result."""

    problem = make_problem(10)

    solver = GeneticAlgorithmSolver(
        generations=20,
    )

    result = solver.solve(problem)

    assert result.solver_name == "Genetic Algorithm"


def test_solution_length() -> None:
    """Solution length should match problem size."""

    problem = make_problem(12)

    result = GeneticAlgorithmSolver().solve(
        problem,
    )

    assert len(result.solution) == 12


def test_solution_binary() -> None:
    """Solution should remain binary."""

    problem = make_problem(20)

    result = GeneticAlgorithmSolver().solve(
        problem,
    )

    assert all(bit in (0, 1) for bit in result.solution)


def test_objective_finite() -> None:
    """Objective value should be finite."""

    problem = make_problem(15)

    result = GeneticAlgorithmSolver().solve(
        problem,
    )

    assert isfinite(result.objective_value)


def test_runtime_non_negative() -> None:
    """Runtime should never be negative."""

    problem = make_problem(8)

    result = GeneticAlgorithmSolver().solve(
        problem,
    )

    assert result.runtime_seconds >= 0.0


def test_generations_reported() -> None:
    """Reported iterations should equal generations."""

    solver = GeneticAlgorithmSolver(
        generations=42,
    )

    result = solver.solve(
        make_problem(5),
    )

    assert result.iterations == 42
