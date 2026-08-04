"""
RNA Folding Explanation Engine.
"""

from __future__ import annotations

from folding.profilers.folding_profiler import FoldingProfile

from decision.models import (
    DecisionReason,
    Evidence,
    Explanation,
)


class FoldingExplainer:
    """
    Explain RNA folding decisions using biological and
    thermodynamic evidence.
    """

    def explain(
        self,
        folding: FoldingProfile,
    ) -> Explanation:
        """Generate an explanation for an RNA folding prediction."""

        reasons: list[DecisionReason] = []

        search = folding.search_space
        thermo = folding.thermodynamics

        #
        # Candidate base pairs
        #

        reasons.append(
            DecisionReason(
                title="Candidate Base Pairs",
                description=(
                    f"{search.variable_count} candidate base pairs "
                    "were generated from the RNA sequence."
                ),
                importance=0.95,
                evidence=[
                    Evidence(
                        name="Candidate Base Pairs",
                        value=search.variable_count,
                        description=("Number of candidate RNA base pairs."),
                        source="BasePairGenerator",
                        weight=0.95,
                    )
                ],
            )
        )

        #
        # Conflict graph
        #

        reasons.append(
            DecisionReason(
                title="Conflict Resolution",
                description=(
                    f"{search.conflict_count} incompatible base-pair conflicts were identified."
                ),
                importance=0.90,
                evidence=[
                    Evidence(
                        name="Conflict Count",
                        value=search.conflict_count,
                        description=("Number of mutually exclusive base pairs."),
                        source="SearchSpaceBuilder",
                        weight=0.90,
                    )
                ],
            )
        )

        #
        # Minimum Free Energy
        #

        reasons.append(
            DecisionReason(
                title="Minimum Free Energy",
                description=(f"Estimated minimum free energy is {thermo.mfe:.2f} kcal/mol."),
                importance=0.95,
            )
        )

        #
        # Thermodynamics
        #

        reasons.append(
            DecisionReason(
                title="Thermodynamic Stability",
                description=(
                    "Nearest-neighbor interactions, stacking energies, "
                    "and loop energetics contributed to the predicted "
                    "RNA secondary structure."
                ),
                importance=0.90,
            )
        )

        return Explanation(
            recommendation="RNA Secondary Structure Prediction",
            confidence=0.95,
            reasons=reasons,
            alternatives=[],
            tradeoffs=[
                "Thermodynamic models approximate biological reality.",
                "Alternative low-energy structures may also exist.",
            ],
            metadata={
                "candidate_pairs": search.variable_count,
                "conflicts": search.conflict_count,
                "mfe": thermo.mfe,
                "dot_bracket": (folding.secondary_structure.dot_bracket),
            },
        )
