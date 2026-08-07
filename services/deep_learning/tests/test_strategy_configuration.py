"""
Tests for strategy configuration model.
"""

from __future__ import annotations

from dl.models.optimization.strategy_configuration import (
    StrategyConfiguration,
)


def test_strategy_configuration_creation() -> None:
    """
    Strategy configuration can be created.
    """

    strategy = StrategyConfiguration(
        strategy_name="quantum_evolutionary",
        solvers=(
            "ising",
            "genetic",
            "tabu",
        ),
        execution_mode="sequential",
        objective="rna_folding",
    )

    assert strategy.strategy_name == ("quantum_evolutionary")

    assert (
        len(
            strategy.solvers,
        )
        == 3
    )

    assert strategy.execution_mode == ("sequential")

    assert strategy.objective == ("rna_folding")
