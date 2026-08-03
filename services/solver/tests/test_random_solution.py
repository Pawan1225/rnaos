from optimization.models.optimization_problem import QUBOProblem
from solver.utils import RandomSolutionGenerator


def make_problem(size: int) -> QUBOProblem:
    """Create a simple QUBO problem."""

    matrix = [[0.0 for _ in range(size)] for _ in range(size)]

    return QUBOProblem(
        matrix=matrix,
        variable_names=[f"x{i}" for i in range(size)],
    )


def test_random_solution_length() -> None:
    """Generated solution should have the correct length."""

    problem = make_problem(20)

    solution = RandomSolutionGenerator.generate(problem)

    assert len(solution) == 20


def test_random_solution_binary() -> None:
    """Generated solution should contain only binary values."""

    problem = make_problem(50)

    solution = RandomSolutionGenerator.generate(problem)

    assert all(value in (0, 1) for value in solution)


def test_multiple_random_solutions() -> None:
    """Repeated generations should always produce valid solutions."""

    problem = make_problem(10)

    for _ in range(100):
        solution = RandomSolutionGenerator.generate(problem)

        assert len(solution) == 10

        assert all(value in (0, 1) for value in solution)
