"""
RNAOS neighborhood operator result model.
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
class NeighborhoodOperatorResult:
    """
    Immutable neighborhood operator result.
    """

    level: int

    state: LocalSearchState
