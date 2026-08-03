from optimization.models.optimization_problem import QUBOProblem
from solver.classical.simulated_annealing import (
    SimulatedAnnealingSolver,
)
from solver.models import SolverFamily


def make_problem(size: int) -> QUBOProblem:
    """Create a simple QUBO problem for testing."""

    matrix = [[0.0 for _ in range(size)] for _ in range(size)]

    return QUBOProblem(
        matrix=matrix,
        variable_names=[f"x{i}" for i in range(size)],
    )


def test_solver_interface() -> None:
    """Verify the solver returns a valid result."""

    problem = make_problem(2)

    solver = SimulatedAnnealingSolver()

    result = solver.solve(problem)

    assert result.solver_name == "Simulated Annealing"
    assert result.variable_count == 2


def test_solver_capabilities() -> None:
    """Verify advertised solver capabilities."""

    solver = SimulatedAnnealingSolver()

    capabilities = solver.capabilities

    assert capabilities.solver_family == SolverFamily.CLASSICAL

    assert capabilities.supports_binary_variables
    assert capabilities.supports_sparse_qubo
    assert capabilities.supports_dense_qubo

    assert not capabilities.quantum
    assert not capabilities.hybrid

    assert capabilities.max_problem_size == 5_000


def test_solver_supports_problem() -> None:
    """Verify compatibility checking."""

    solver = SimulatedAnnealingSolver()

    assert solver.supports(make_problem(10))
    assert solver.supports(make_problem(5_000))
    assert not solver.supports(make_problem(5_001))
