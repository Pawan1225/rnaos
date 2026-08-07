"""
RNAOS hybrid strategy configuration model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class StrategyConfiguration:
    """
    Immutable hybrid solver strategy configuration.
    """

    strategy_name: str

    solvers: tuple[str, ...]

    execution_mode: str

    objective: str
