"""
RNAOS model routing decision model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class ModelRoute:
    """
    Immutable model routing decision.
    """

    selected_model: str

    score: float

    reasoning: str
