"""
RNAOS differential evolution mutation engine.
"""

from __future__ import annotations

from dl.models.optimization.differential_vector import (
    DifferentialVector,
)
from dl.models.optimization.mutation_vector_result import (
    MutationVectorResult,
)


class DifferentialMutationEngine:
    """
    Performs differential mutation.

    Formula:

    mutant = a + F * (b - c)
    """

    def mutate(
        self,
        base: DifferentialVector,
        vector_b: DifferentialVector,
        vector_c: DifferentialVector,
        factor: float,
    ) -> MutationVectorResult:
        """
        Generate mutant vector.
        """

        if factor < 0:
            raise ValueError(
                "Mutation factor must be non-negative",
            )

        if not (len(base.values) == len(vector_b.values) == len(vector_c.values)):
            raise ValueError(
                "Vector dimensions must match",
            )

        values = tuple(
            a + factor * (b - c)
            for a, b, c in zip(
                base.values,
                vector_b.values,
                vector_c.values,
                strict=True,
            )
        )

        mutant = DifferentialVector(
            vector_id=-1,
            values=values,
            fitness=0.0,
            generation=base.generation + 1,
        )

        return MutationVectorResult(
            base_vector_id=base.vector_id,
            mutant_vector=mutant,
        )
