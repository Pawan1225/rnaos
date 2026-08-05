"""
RNAOS sequence feature models.
"""

from __future__ import annotations

from dataclasses import dataclass

from biology.models.nucleotide_counts import (
    NucleotideCounts,
)


@dataclass(slots=True, frozen=True)
class SequenceFeatures:
    """
    Fundamental RNA sequence features.
    """

    sequence: str

    length: int

    nucleotide_counts: NucleotideCounts

    purine_count: int

    pyrimidine_count: int

    is_valid: bool
