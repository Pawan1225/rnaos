"""
RNAOS differential evolution recombination engine.
"""

from __future__ import annotations

import random

from dl.models.optimization.differential_vector import (
    DifferentialVector,
)
from dl.models.optimization.recombination_result import (
    RecombinationResult,
)


class RecombinationEngine:
    """
    Combines target and mutant vectors.
    """

    def recombine(
        self,
        target: DifferentialVector,
        mutant: DifferentialVector,
        crossover_rate: float,
        seed: int = 42,
    ) -> RecombinationResult:
        """
        Perform binomial crossover.
        """

        if not 0.0 <= crossover_rate <= 1.0:
            raise ValueError(
                "Crossover rate must be between 0 and 1",
            )

        if len(target.values) != len(
            mutant.values,
        ):
            raise ValueError(
                "Vector dimensions must match",
            )

        rng = random.Random(seed)

        values: list[float] = []

        changed = 0

        for target_value, mutant_value in zip(
            target.values,
            mutant.values,
            strict=True,
        ):
            if rng.random() < crossover_rate:
                values.append(
                    mutant_value,
                )
                changed += 1
            else:
                values.append(
                    target_value,
                )

        trial = DifferentialVector(
            vector_id=-1,
            values=tuple(values),
            fitness=0.0,
            generation=target.generation + 1,
        )

        return RecombinationResult(
            target_id=target.vector_id,
            trial_vector=trial,
            changed_dimensions=changed,
        )
