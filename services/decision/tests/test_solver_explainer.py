from decision.explainers import RuleBasedSolverExplainer
from optimization.models.optimization_problem import QUBOProblem
from solver.classical.exact_solver import ExactSolver
from solver.classical.genetic_algorithm import (
    GeneticAlgorithmSolver,
)


def create_problem(
    size: int,
    density: float,
) -> QUBOProblem:
    """Create a minimal QUBO problem for testing."""

    return QUBOProblem(
        matrix=[[0.0] * size for _ in range(size)],
        variable_names=[f"x{i}" for i in range(size)],
        metadata={
            "qubo_density": density,
        },
    )


def test_exact_solver_explanation():
    """Test explanation generation for the Exact Solver."""

    problem = create_problem(
        size=10,
        density=0.20,
    )

    solver = ExactSolver()

    alternatives = [
        GeneticAlgorithmSolver(),
    ]

    explanation = RuleBasedSolverExplainer().explain(
        problem,
        solver,
        alternatives,
    )

    assert explanation.recommendation == "Exact Solver"

    assert explanation.confidence > 0.0

    assert len(explanation.reasons) == 3

    assert len(explanation.tradeoffs) > 0

    assert "Genetic Algorithm" in explanation.alternatives


def test_classical_solver_explanation():
    """Test explanation generation for a classical solver."""

    problem = create_problem(
        size=75,
        density=0.80,
    )

    solver = GeneticAlgorithmSolver()

    explanation = RuleBasedSolverExplainer().explain(
        problem,
        solver,
        [],
    )

    assert explanation.recommendation == "Genetic Algorithm"

    assert explanation.confidence > 0.0

    assert len(explanation.reasons) == 3

    assert len(explanation.tradeoffs) > 0

    assert len(explanation.alternatives) > 0


def test_metadata():
    """Metadata should preserve optimization context."""

    problem = create_problem(
        size=50,
        density=0.65,
    )

    solver = ExactSolver()

    explanation = RuleBasedSolverExplainer().explain(
        problem,
        solver,
        [],
    )

    assert explanation.metadata["problem_size"] == 50

    assert explanation.metadata["qubo_density"] == 0.65

    assert explanation.metadata["solver_family"] == solver.capabilities.solver_family.value


def test_confidence_range():
    """Confidence must remain within [0,1]."""

    problem = create_problem(
        size=500,
        density=0.95,
    )

    solver = GeneticAlgorithmSolver()

    explanation = RuleBasedSolverExplainer().explain(
        problem,
        solver,
        [],
    )

    assert 0.0 <= explanation.confidence <= 1.0
