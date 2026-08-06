"""
RNAOS thermodynamic profile models.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class ThermodynamicProfile:
    """
    Thermodynamic feature summary for an RNA sequence.

    The values in this profile are deterministic heuristic
    descriptors intended for downstream AI, ML, DL, QML,
    and optimization modules. They do not replace
    thermodynamic folding engines such as ViennaRNA.
    """

    gc_stability: float

    au_stability: float

    pair_density: float

    stem_stability: float

    stability_index: float

    approximate_free_energy: float
