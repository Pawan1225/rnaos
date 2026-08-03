"""
RNA Folding QUBO Generator.

Generates a biologically meaningful QUBO representation
from an RNA Folding search space.
"""

from __future__ import annotations

from folding.profilers.folding_profiler import (
    FoldingProfile,
)

from optimization.models.optimization_problem import (
    QUBOProblem,
)

# ----------------------------------------------------------------------
# QUBO parameters
# ----------------------------------------------------------------------

CONFLICT_PENALTY = 5.0

DEFAULT_BASE_PAIR_REWARD = -1.0


class QUBOGenerator:
    """
    Generate a Version 1 RNA Folding QUBO.

    Version 1
    ---------
    * Uniform reward for selecting a candidate base pair.
    * Uniform penalty for incompatible base pairs.

    Future versions
    ---------------
    * Candidate-specific thermodynamic energies
    * Adaptive penalty scaling
    * Soft constraints
    * Pseudoknot support
    """

    def generate(
        self,
        folding_profile: FoldingProfile,
        variable_names: list[str],
    ) -> QUBOProblem:
        """
        Generate a QUBO matrix for RNA folding.

        Parameters
        ----------
        folding_profile
            Biological folding profile.

        variable_names
            Binary decision variables corresponding to
            candidate RNA base pairs.
        """

        size = len(variable_names)

        matrix = [[0.0 for _ in range(size)] for _ in range(size)]

        # --------------------------------------------------------------
        # Diagonal terms
        #
        # Version 1:
        # Every candidate receives the same reward.
        #
        # Version 2:
        # Replace with nearest-neighbor thermodynamic
        # energies for each candidate.
        # --------------------------------------------------------------

        for i in range(size):
            matrix[i][i] = DEFAULT_BASE_PAIR_REWARD

        # --------------------------------------------------------------
        # Off-diagonal conflict penalties
        # --------------------------------------------------------------

        for edge in folding_profile.search_space.conflicts:
            matrix[edge.first][edge.second] += CONFLICT_PENALTY
            matrix[edge.second][edge.first] += CONFLICT_PENALTY

        return QUBOProblem(
            matrix=matrix,
            variable_names=variable_names,
            penalty=CONFLICT_PENALTY,
            metadata={
                "reward_model": "uniform",
                "base_pair_reward": DEFAULT_BASE_PAIR_REWARD,
                "candidate_pair_count": size,
                "conflict_count": (folding_profile.search_space.conflict_count),
                "search_space_density": (
                    folding_profile.search_space_density
                    if hasattr(
                        folding_profile.search_space,
                        "search_space_density",
                    )
                    else None
                ),
                "qubo_version": "1.0",
            },
        )
