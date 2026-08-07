"""
RNAOS Ising optimization result model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class IsingResult:
    """
    Immutable Ising optimization result.
    """

    spins: tuple[int, ...]

    energy: float

    iterations: int

    converged: bool
