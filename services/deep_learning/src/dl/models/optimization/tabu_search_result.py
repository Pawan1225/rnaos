"""
RNAOS tabu search result model.
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
class TabuSearchResult:
    """
    Immutable tabu search result.
    """

    best_state: LocalSearchState

    iterations: int

    tabu_size: int
