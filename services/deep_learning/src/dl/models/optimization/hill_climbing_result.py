"""
RNAOS hill climbing result model.
"""

from __future__ import annotations

from dataclasses import dataclass

from dl.models.optimization.local_search_state import (
    LocalSearchState,
)


@dataclass(
    slots=True,
    frozen=True,
)
class HillClimbingResult:
    """
    Immutable hill climbing result.
    """

    best_state: LocalSearchState

    iterations: int

    improved: bool
