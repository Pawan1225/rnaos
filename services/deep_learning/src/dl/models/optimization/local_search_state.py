"""
RNAOS local search state model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class LocalSearchState:
    """
    Immutable local search state.
    """

    state_id: int

    solution: tuple[int, ...]

    energy: float

    iteration: int
