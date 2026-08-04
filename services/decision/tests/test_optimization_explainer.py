from decision.explainers import OptimizationExplainer
from optimization.models.optimization_problem import QUBOProblem


def create_problem(
    size: int,
    penalty: float,
) -> QUBOProblem:
    """Create a minimal QUBO problem."""

    return QUBOProblem(
        matrix=[[0.0] * size for _ in range(size)],
        variable_names=[f"x{i}" for i in range(size)],
        penalty=penalty,
    )


def test_optimization_explanation():
    """Test optimization explanation generation."""

    problem = create_problem(
        size=42,
        penalty=8.0,
    )

    explanation = OptimizationExplainer().explain(problem)

    assert explanation.recommendation == "Scientific QUBO Formulation"

    assert explanation.confidence == 1.0

    assert len(explanation.reasons) == 4

    assert explanation.metadata["variables"] == 42

    assert explanation.metadata["penalty"] == 8.0


def test_penalty_metadata():
    """Penalty metadata should be preserved."""

    problem = create_problem(
        size=10,
        penalty=5.0,
    )

    explanation = OptimizationExplainer().explain(problem)

    assert explanation.metadata["penalty"] == 5.0


def test_tradeoffs_present():
    """Trade-offs should always be generated."""

    problem = create_problem(
        size=25,
        penalty=10.0,
    )

    explanation = OptimizationExplainer().explain(problem)

    assert len(explanation.tradeoffs) > 0


def test_confidence_range():
    """Confidence should remain within [0,1]."""

    problem = create_problem(
        size=100,
        penalty=15.0,
    )

    explanation = OptimizationExplainer().explain(problem)

    assert 0.0 <= explanation.confidence <= 1.0
