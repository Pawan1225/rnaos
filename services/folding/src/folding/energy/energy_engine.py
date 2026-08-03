"""
RNA Thermodynamic Engine.

Evaluates RNA secondary structures using ViennaRNA and produces
thermodynamic profiles for optimization.
"""

from __future__ import annotations

from folding.energy.thermodynamic_profile import ThermodynamicProfile
from folding.engines.vienna_engine import ViennaEngine


class ThermodynamicEngine:
    """
    Evaluate RNA thermodynamic properties.
    """

    def __init__(self) -> None:
        self.vienna = ViennaEngine()

    def evaluate(
        self,
        sequence: str,
        candidate_structure: str,
    ) -> ThermodynamicProfile:
        """
        Evaluate a candidate secondary structure relative to
        the minimum free energy (MFE) structure.
        """

        mfe_result = self.vienna.fold(sequence)

        candidate_energy = self.vienna.evaluate(
            sequence,
            candidate_structure,
        )

        energy_gap = candidate_energy - mfe_result.mfe

        normalized_gap = energy_gap / max(abs(mfe_result.mfe), 1.0)

        return ThermodynamicProfile(
            sequence=sequence,
            dot_bracket=candidate_structure,
            mfe=mfe_result.mfe,
            candidate_energy=candidate_energy,
            energy_gap=energy_gap,
            normalized_gap=normalized_gap,
        )
