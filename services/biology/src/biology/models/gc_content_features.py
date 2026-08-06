"""
RNAOS GC content feature models.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class GCContentFeatures:
    """
    GC composition statistics for an RNA sequence.

    All composition values are normalized fractions
    in the range [0.0, 1.0] unless otherwise noted.
    """

    gc_content: float

    au_content: float

    gc_skew: float

    gc_au_ratio: float

    purine_pyrimidine_ratio: float
