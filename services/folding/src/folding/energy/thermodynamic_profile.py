"""
RNA Thermodynamic Profile.

Represents the thermodynamic evaluation of an RNA secondary
structure relative to the minimum free energy (MFE) structure.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class ThermodynamicProfile:
    """
    Thermodynamic properties of an RNA structure.
    """

    sequence: str

    dot_bracket: str

    mfe: float

    candidate_energy: float

    energy_gap: float

    normalized_gap: float

    @property
    def is_optimal(self) -> bool:
        """
        Return True if the candidate structure has the same
        energy as the minimum free energy structure.
        """
        return abs(self.energy_gap) < 1e-6
