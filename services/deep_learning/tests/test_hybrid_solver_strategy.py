"""
Tests for hybrid solver strategy model.
"""

from __future__ import annotations

from dl.models.optimization.hybrid_solver_strategy import (
    HybridSolverStrategy,
)
from dl.models.optimization.solver_combination_rule import (
    SolverCombinationRule,
)
from dl.models.optimization.strategy_configuration import (
    StrategyConfiguration,
)


def test_hybrid_solver_strategy_creation() -> None:
    """
    Hybrid solver strategy can be created.
    """

    configuration = StrategyConfiguration(
        strategy_name="quantum_evolutionary",
        solvers=(
            "ising",
            "genetic",
            "tabu",
        ),
        execution_mode="sequential",
        objective="rna_folding",
    )

    rules = (
        SolverCombinationRule(
            primary_solver="ising",
            secondary_solver="genetic",
            refinement_solver="tabu",
            condition="complex_problem",
        ),
    )

    strategy = HybridSolverStrategy(
        configuration=configuration,
        rules=rules,
        active=True,
    )

    assert strategy.configuration.strategy_name == ("quantum_evolutionary")

    assert (
        len(
            strategy.rules,
        )
        == 1
    )

    assert strategy.rules[0].primary_solver == "ising"

    assert strategy.active is True
