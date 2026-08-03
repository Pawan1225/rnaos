"""
Scientific QUBO Validation.

Sprint 6.6
"""

from __future__ import annotations

from dataclasses import dataclass

from folding.profilers.folding_profiler import FoldingProfile
from folding.thermodynamics import ScientificEnergyModel


@dataclass(slots=True)
class ValidationReport:
    """
    Validation metrics comparing RNAOS against ViennaRNA.
    """

    vienna_mfe: float
    estimated_energy: float
    absolute_error: float
    relative_error: float

    candidate_pairs: int
    conflicts: int


class QUBOValidator:
    """
    Validate the scientific RNA folding model.
    """

    def __init__(self) -> None:
        self.energy_model = ScientificEnergyModel()

    def validate(
        self,
        folding: FoldingProfile,
    ) -> ValidationReport:
        total_energy = 0.0

        previous = None

        for candidate in folding.search_space.candidates:
            estimate = self.energy_model.estimate(
                candidate,
                previous,
            )

            total_energy += estimate.total_energy

            previous = candidate

        mfe = folding.thermodynamics.mfe

        absolute_error = abs(total_energy - mfe)

        relative_error = absolute_error / max(abs(mfe), 1.0)

        return ValidationReport(
            vienna_mfe=mfe,
            estimated_energy=total_energy,
            absolute_error=absolute_error,
            relative_error=relative_error,
            candidate_pairs=folding.search_space.variable_count,
            conflicts=folding.search_space.conflict_count,
        )
