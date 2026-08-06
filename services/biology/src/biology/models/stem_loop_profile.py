"""
RNAOS stem-loop profile models.
"""

from __future__ import annotations

from dataclasses import dataclass

from biology.models.stem_loop_candidate import (
    StemLoopCandidate,
)


@dataclass(slots=True, frozen=True)
class StemLoopProfile:
    """
    Summary of heuristic stem-loop analysis.

    The profile aggregates all candidate stem-loop structures
    identified within an RNA sequence and provides summary
    statistics that can be consumed by downstream AI, machine
    learning, deep learning, and quantum optimization modules.
    """

    candidates: tuple[StemLoopCandidate, ...]

    estimated_stems: int

    estimated_loops: int

    average_stem_length: float

    average_loop_length: float
