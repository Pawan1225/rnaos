"""
Scientific RNA Energy Model.

Sprint 6.5

Combines all thermodynamic contributions into
a unified energy estimate.
"""

from __future__ import annotations

from dataclasses import dataclass

from folding.basepairs.basepair_generator import BasePairCandidate
from folding.thermodynamics.loops import (
    LoopEnergyModel,
)
from folding.thermodynamics.nearest_neighbor import (
    NearestNeighborModel,
)
from folding.thermodynamics.stacking import (
    StackingEnergyModel,
)


@dataclass(frozen=True, slots=True)
class ScientificEnergyEstimate:
    """
    Complete thermodynamic estimate for one RNA candidate pair.
    """

    base_pair_energy: float
    stacking_energy: float
    loop_energy: float
    total_energy: float


class ScientificEnergyModel:
    """
    Aggregate all thermodynamic models.
    """

    def __init__(self) -> None:
        self.nn = NearestNeighborModel()
        self.stacking = StackingEnergyModel()
        self.loops = LoopEnergyModel()

    def estimate(
        self,
        candidate: BasePairCandidate,
        previous: BasePairCandidate | None = None,
    ) -> ScientificEnergyEstimate:
        """
        Estimate total thermodynamic contribution.
        """

        base_energy = self.nn.pair_energy(candidate)

        stack_energy = 0.0

        if previous is not None:
            stack_energy = self.stacking.stacking_energy(
                previous,
                candidate,
            )

        loop_size = candidate.right - candidate.left - 1

        loop_energy = self.loops.hairpin_energy(
            loop_size,
        )

        total = base_energy + stack_energy + loop_energy

        return ScientificEnergyEstimate(
            base_pair_energy=base_energy,
            stacking_energy=stack_energy,
            loop_energy=loop_energy,
            total_energy=total,
        )
