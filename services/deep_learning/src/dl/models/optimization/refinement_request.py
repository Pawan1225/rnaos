"""
RNAOS refinement request model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class RefinementRequest:
    """
    Immutable refinement request.
    """

    candidate_id: int

    structure: tuple[str, ...]

    current_energy: float

    strategy: str
