from optimization.models.optimization_problem import QUBOProblem
from solver.utils import QUBOObjectiveEvaluator


def test_qubo_objective() -> None:
    """Verify QUBO objective evaluation."""

    problem = QUBOProblem(
        matrix=[
            [-1.0, 0.0],
            [0.0, -2.0],
        ],
        variable_names=[
            "x0",
            "x1",
        ],
    )

    value = QUBOObjectiveEvaluator.evaluate(
        problem,
        [1, 1],
    )

    assert value == -3.0


def test_zero_solution() -> None:
    """Zero solution should have zero objective."""

    problem = QUBOProblem(
        matrix=[
            [-1.0, 0.0],
            [0.0, -2.0],
        ],
        variable_names=[
            "x0",
            "x1",
        ],
    )

    value = QUBOObjectiveEvaluator.evaluate(
        problem,
        [0, 0],
    )

    assert value == 0.0
