"""
RNAOS objective function models.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class ObjectiveFunction:
    """
    Immutable optimization objective.
    """

    name: str

    terms: tuple[float, ...]

    minimize: bool = True
