"""
RNAOS motif occurrence models.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class MotifOccurrence:
    """
    Represents occurrences of a biological motif.
    """

    motif: str

    count: int

    positions: tuple[int, ...]
