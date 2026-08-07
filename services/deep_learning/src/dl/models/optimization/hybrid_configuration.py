"""
RNAOS hybrid optimization configuration.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class HybridConfiguration:
    """
    Immutable hybrid optimizer configuration.
    """

    enable_qubo: bool

    enable_annealing: bool

    enable_tensor: bool

    ensemble_mode: str

    max_solvers: int

    selection_strategy: str
