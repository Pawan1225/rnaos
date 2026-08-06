"""
RNAOS stem-loop candidate models.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class StemLoopCandidate:
    """
    Represents a candidate RNA stem-loop (hairpin) structure.

    The detector uses heuristic structural analysis to identify
    complementary stem regions separated by a loop. These
    candidates are intended as biologically meaningful structural
    features for downstream AI, ML, and Quantum modules rather
    than thermodynamically optimal structures.
    """

    stem_start: int

    stem_end: int

    loop_start: int

    loop_end: int

    stem_length: int

    loop_length: int

    score: float
