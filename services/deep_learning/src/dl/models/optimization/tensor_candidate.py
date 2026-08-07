"""
RNAOS tensor search candidate models.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class TensorCandidate:
    """
    Immutable tensor search candidate.
    """

    state: tuple[int, ...]

    score: float
