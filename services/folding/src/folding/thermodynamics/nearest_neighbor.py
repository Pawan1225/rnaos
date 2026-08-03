"""
Nearest-neighbor energy model.

Sprint 6.2

Version 1 estimates the intrinsic thermodynamic contribution of a
candidate RNA base pair using canonical base-pair energies.

Future versions will incorporate:

- Turner nearest-neighbor stacking tables
- Sequence-dependent interactions
- Terminal penalties
- Dangling ends
"""

from __future__ import annotations

from dataclasses import dataclass

from folding.basepairs.basepair_generator import BasePairCandidate
from folding.thermodynamics import EnergyParameters


@dataclass(frozen=True, slots=True)
class PairEnergyEstimate:
    """
    Energy estimate for a candidate RNA base pair.
    """

    pair: str
    energy: float
    hydrogen_bonds: int


class NearestNeighborModel:
    """
    Estimate thermodynamic properties of RNA base pairs.
    """

    def estimate(
        self,
        candidate: BasePairCandidate,
    ) -> PairEnergyEstimate:
        """
        Estimate the intrinsic energy of a candidate pair.
        """

        pair = (candidate.left_base + candidate.right_base).upper()

        metadata = EnergyParameters.metadata(pair)

        return PairEnergyEstimate(
            pair=pair,
            energy=metadata.energy,
            hydrogen_bonds=metadata.hydrogen_bonds,
        )

    def pair_energy(
        self,
        candidate: BasePairCandidate,
    ) -> float:
        """
        Convenience wrapper returning only the energy value.
        """

        return self.estimate(candidate).energy
