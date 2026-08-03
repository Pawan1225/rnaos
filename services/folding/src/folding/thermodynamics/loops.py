"""
RNA Loop Energy Model.

Sprint 6.4

Version 1 implements simplified loop energy penalties.

Future versions will include Turner loop parameters.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class LoopEnergyEstimate:
    """
    Loop energy estimate.
    """

    loop_type: str
    energy: float


class LoopEnergyModel:
    """
    Estimate RNA loop energies.
    """

    def hairpin(self, loop_size: int) -> LoopEnergyEstimate:
        if loop_size < 3:
            return LoopEnergyEstimate(
                loop_type="invalid",
                energy=100.0,
            )

        return LoopEnergyEstimate(
            loop_type="hairpin",
            energy=3.0 + 0.2 * loop_size,
        )

    def internal(self, left_size: int, right_size: int) -> LoopEnergyEstimate:
        return LoopEnergyEstimate(
            loop_type="internal",
            energy=1.5 + 0.3 * (left_size + right_size),
        )

    def bulge(self, bulge_size: int) -> LoopEnergyEstimate:
        return LoopEnergyEstimate(
            loop_type="bulge",
            energy=2.0 + 0.3 * bulge_size,
        )

    def multiloop(self, branches: int) -> LoopEnergyEstimate:
        return LoopEnergyEstimate(
            loop_type="multiloop",
            energy=4.0 + 0.4 * branches,
        )

    #
    # Convenience wrappers
    #

    def hairpin_energy(self, loop_size: int) -> float:
        return self.hairpin(loop_size).energy

    def internal_loop_energy(
        self,
        left_size: int,
        right_size: int,
    ) -> float:
        return self.internal(left_size, right_size).energy

    def bulge_energy(self, bulge_size: int) -> float:
        return self.bulge(bulge_size).energy

    def multiloop_energy(self, branches: int) -> float:
        return self.multiloop(branches).energy
