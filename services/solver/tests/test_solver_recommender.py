from optimization.models.optimization_problem import QUBOProblem
from solver.classical.exact_solver import ExactSolver
from solver.classical.genetic_algorithm import GeneticAlgorithmSolver
from solver.classical.simulated_annealing import (
    SimulatedAnnealingSolver,
)
from solver.recommender.solver_recommender import (
    SolverRecommender,
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


def test_prefers_exact_solver() -> None:
    """Exact solver should be preferred for small problems."""

    recommender = SolverRecommender()

    solver = recommender.recommend(
        make_problem(5),
        [
            SimulatedAnnealingSolver(),
            GeneticAlgorithmSolver(),
            ExactSolver(),
        ],
    )

    assert solver.name == "Exact Solver"


def test_skips_unsupported_solver() -> None:
    """Exact solver should be skipped for large problems."""

    recommender = SolverRecommender()

    solver = recommender.recommend(
        make_problem(100),
        [
            SimulatedAnnealingSolver(),
            GeneticAlgorithmSolver(),
            ExactSolver(),
        ],
    )

    assert solver.name != "Exact Solver"


def test_returns_supported_solver() -> None:
    """Returned solver should support the problem."""

    recommender = SolverRecommender()

    problem = make_problem(100)

    solver = recommender.recommend(
        problem,
        [
            SimulatedAnnealingSolver(),
            GeneticAlgorithmSolver(),
            ExactSolver(),
        ],
    )

    assert solver.supports(problem)
