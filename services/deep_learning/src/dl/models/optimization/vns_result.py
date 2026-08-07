"""
RNAOS variable neighborhood search result model.
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
class VNSResult:
    """
    Immutable VNS optimization result.
    """

    best_state: LocalSearchState

    neighborhood_level: int

    iterations: int
