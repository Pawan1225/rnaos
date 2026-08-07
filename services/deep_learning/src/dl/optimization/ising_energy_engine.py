"""
RNAOS Ising energy evaluator.
"""

from __future__ import annotations

from dl.models.optimization.ising_model import (
    IsingModel,
)


class IsingEnergyEngine:
    """
    Calculates Ising Hamiltonian energy.

    E(s) = h*s + s*J*s + offset
    """

    def calculate(
        self,
        model: IsingModel,
        spins: tuple[int, ...],
    ) -> float:
        """
        Calculate Ising energy.
        """

        if len(spins) != len(
            model.variables,
        ):
            raise ValueError(
                "Spin dimension mismatch",
            )

        energy = model.offset

        for index, spin in enumerate(
            spins,
        ):
            energy += model.local_fields[index] * spin

        for i, row in enumerate(
            model.couplings,
        ):
            for j, coupling in enumerate(
                row,
            ):
                energy += coupling * spins[i] * spins[j]

        return energy
