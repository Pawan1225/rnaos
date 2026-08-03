"""
RNA stacking energy model.

Sprint 6.3

Version 1 implements a simplified approximation of
base-pair stacking interactions.

Future versions will use Turner nearest-neighbor
stacking parameters.
"""

from __future__ import annotations

from dataclasses import dataclass

from folding.basepairs.basepair_generator import BasePairCandidate


@dataclass(frozen=True, slots=True)
class StackingEnergyEstimate:
    """
    Stacking interaction between two RNA base pairs.
    """

    energy: float
    adjacent: bool
    interaction_type: str


class StackingEnergyModel:
    """
    Estimate stacking stabilization between two base pairs.
    """

    def estimate(
        self,
        first: BasePairCandidate,
        second: BasePairCandidate,
    ) -> StackingEnergyEstimate:
        """
        Estimate stacking stabilization.
        """

        #
        # Adjacent helix
        #

        if second.left == first.left + 1 and second.right == first.right - 1:
            return StackingEnergyEstimate(
                energy=-0.5,
                adjacent=True,
                interaction_type="adjacent",
            )

        #
        # Near-adjacent
        #

        if abs(second.left - first.left) <= 2 and abs(second.right - first.right) <= 2:
            return StackingEnergyEstimate(
                energy=-0.2,
                adjacent=False,
                interaction_type="near",
            )

        return StackingEnergyEstimate(
            energy=0.0,
            adjacent=False,
            interaction_type="none",
        )

    def stacking_energy(
        self,
        first: BasePairCandidate,
        second: BasePairCandidate,
    ) -> float:
        """
        Convenience wrapper.
        """

        return self.estimate(
            first,
            second,
        ).energy
