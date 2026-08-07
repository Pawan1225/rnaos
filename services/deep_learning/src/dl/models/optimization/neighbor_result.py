"""
RNAOS neighbor generation result model.
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
class NeighborResult:
    """
    Immutable neighbor generation result.
    """

    source_id: int

    neighbors: tuple[LocalSearchState, ...]
