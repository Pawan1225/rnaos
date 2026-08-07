"""
RNAOS optimization ensemble models.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class EnsembleResult:
    """
    Immutable ensemble optimization result.
    """

    selected_solver: str

    energy: float

    candidate_count: int
