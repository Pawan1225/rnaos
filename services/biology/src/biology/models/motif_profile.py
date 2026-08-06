"""
RNAOS motif profile models.
"""

from __future__ import annotations

from dataclasses import dataclass

from biology.models.motif_occurrence import (
    MotifOccurrence,
)


@dataclass(slots=True, frozen=True)
class MotifProfile:
    """
    Complete motif analysis profile.
    """

    canonical: tuple[MotifOccurrence, ...]

    repetitive: tuple[MotifOccurrence, ...]

    structural: tuple[MotifOccurrence, ...]

    regulatory: tuple[MotifOccurrence, ...]

    custom: tuple[MotifOccurrence, ...]
