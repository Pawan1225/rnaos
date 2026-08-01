import pytest
from solver_portfolio.greedy.greedy_solver import (
    GreedySolver,
)
from solver_portfolio.registry.solver_registry import (
    SolverRegistry,
)


def test_register_solver():
    registry = SolverRegistry()

    registry.register(
        GreedySolver(),
    )

    assert registry.exists("greedy")


def test_get_solver():
    registry = SolverRegistry()

    registry.register(
        GreedySolver(),
    )

    solver = registry.get("greedy")

    assert solver.name == "greedy"


def test_unknown_solver():
    registry = SolverRegistry()

    with pytest.raises(KeyError):
        registry.get("unknown")


def test_names():
    registry = SolverRegistry()

    registry.register(
        GreedySolver(),
    )

    assert "greedy" in registry.names()
