"""
Scientific RNA Folding QUBO Generator.

Sprint 6.5.2

Generates an energy-aware QUBO by consuming the
ScientificEnergyModel rather than directly performing
thermodynamic calculations.
"""

from __future__ import annotations

from folding.profilers.folding_profiler import FoldingProfile
from folding.thermodynamics import ScientificEnergyModel

from optimization.models.optimization_problem import QUBOProblem


class ScientificQUBOGenerator:
    """
    Generate a scientific RNA folding QUBO.
    """

    def __init__(self) -> None:
        self.energy_model = ScientificEnergyModel()
        self.conflict_penalty = 8.0

    def generate(
        self,
        folding: FoldingProfile,
        variables: list[str],
    ) -> QUBOProblem:
        """
        Generate an energy-weighted RNA folding QUBO.
        """

        candidates = folding.search_space.candidates
        n = len(candidates)

        matrix = [[0.0] * n for _ in range(n)]

        #
        # Diagonal terms (thermodynamic energy)
        #

        previous = None

        for i, candidate in enumerate(candidates):
            estimate = self.energy_model.estimate(
                candidate,
                previous,
            )

            matrix[i][i] = estimate.total_energy

            previous = candidate

        #
        # Conflict penalties
        #

        for edge in folding.search_space.conflicts:
            i = edge.first
            j = edge.second

            matrix[i][j] += self.conflict_penalty
            matrix[j][i] += self.conflict_penalty

        #
        # Metadata
        #

        metadata = {
            "candidate_pairs": len(candidates),
            "conflicts": len(folding.search_space.conflicts),
            "generator": "ScientificQUBOGenerator",
        }

        return QUBOProblem(
            matrix=matrix,
            variable_names=variables,
            penalty=self.conflict_penalty,
            metadata=metadata,
        )
