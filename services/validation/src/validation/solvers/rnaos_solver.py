"""
RNAOS structure optimization solver.
"""

from __future__ import annotations

from validation.generation.combined_candidate_generator import (
    CombinedCandidateGenerator,
)
from validation.optimization.energy_aware_optimizer import (
    EnergyAwareOptimizer,
)
from validation.structure.rna_constraint_validator import (
    RNAConstraintValidator,
)
from validation.structure.structure_validator import (
    StructureValidator,
)


class RNAOSSolver:
    """
    RNAOS solver.

    Generates optimized RNA secondary structures.
    """

    def __init__(
        self,
        evaluator,
    ) -> None:

        self.generator = CombinedCandidateGenerator()

        self.validator = RNAConstraintValidator()

        self.structure_validator = StructureValidator()

        self.optimizer = EnergyAwareOptimizer(
            generator=self.generator,
            validator=self.validator,
            evaluator=evaluator,
        )

    def solve(
        self,
        sequence: str,
    ) -> str:
        """
        Generate optimized structure.
        """

        structure = self.optimizer.optimize(
            sequence,
        )

        if not self.structure_validator.validate(
            structure,
        ):
            return "." * len(sequence)

        return structure
