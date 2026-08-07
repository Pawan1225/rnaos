"""
RNAOS tabu list result model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class TabuListResult:
    """
    Immutable tabu list operation result.
    """

    states: tuple[tuple[int, ...], ...]

    size: int
