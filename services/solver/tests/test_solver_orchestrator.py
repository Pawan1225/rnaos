from optimization.models.optimization_problem import QUBOProblem
from solver.classical.exact_solver import ExactSolver
from solver.classical.genetic_algorithm import GeneticAlgorithmSolver
from solver.classical.simulated_annealing import SimulatedAnnealingSolver
from solver.orchestrator.solver_orchestrator import SolverOrchestrator


def make_problem(size: int) -> QUBOProblem:
    """Create a simple QUBO problem."""

    matrix = [[0.0 for _ in range(size)] for _ in range(size)]

    for i in range(size):
        matrix[i][i] = -1.0

    return QUBOProblem(
        matrix=matrix,
        variable_names=[f"x{i}" for i in range(size)],
    )


def test_orchestrator_runs_all_solvers() -> None:
    """All compatible solvers should execute."""

    orchestrator = SolverOrchestrator(
        [
            SimulatedAnnealingSolver(),
            GeneticAlgorithmSolver(),
            ExactSolver(),
        ],
    )

    results = orchestrator.solve(
        make_problem(5),
    )

    assert len(results) == 3


def test_results_are_ranked() -> None:
    """Results should be sorted by objective value."""

    orchestrator = SolverOrchestrator(
        [
            SimulatedAnnealingSolver(),
            GeneticAlgorithmSolver(),
            ExactSolver(),
        ],
    )

    results = orchestrator.solve(
        make_problem(5),
    )

    objectives = [result.objective_value for result in results]

    assert objectives == sorted(objectives)


def test_best_solver() -> None:
    """best_solver() should return the top-ranked result."""

    orchestrator = SolverOrchestrator(
        [
            SimulatedAnnealingSolver(),
            GeneticAlgorithmSolver(),
            ExactSolver(),
        ],
    )

    problem = make_problem(5)

    results = orchestrator.solve(problem)

    best = orchestrator.best_solver(problem)

    expected = results[0]

    assert best.solver_name == expected.solver_name

    assert best.objective_value == expected.objective_value

    assert best.solution == expected.solution

    assert best.iterations == expected.iterations


def test_unsupported_solver_filtered() -> None:
    """Exact solver should be skipped for oversized problems."""

    orchestrator = SolverOrchestrator(
        [
            SimulatedAnnealingSolver(),
            GeneticAlgorithmSolver(),
            ExactSolver(),
        ],
    )

    results = orchestrator.solve(
        make_problem(30),
    )

    assert len(results) == 2

    assert all(result.solver_name != "Exact Solver" for result in results)
