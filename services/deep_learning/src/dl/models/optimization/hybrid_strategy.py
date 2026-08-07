"""
RNAOS hybrid solver strategy model.
"""

from __future__ import annotations

from dataclasses import dataclass

from dl.models.optimization.solver_combination_rule import (
    SolverCombinationRule,
)
from dl.models.optimization.strategy_configuration import (
    StrategyConfiguration,
)


@dataclass(
    slots=True,
    frozen=True,
)
class HybridStrategy:
    """
    Immutable hybrid solver strategy.
    """

    configuration: StrategyConfiguration

    rules: tuple[
        SolverCombinationRule,
        ...,
    ]

    confidence: float
