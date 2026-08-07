"""
RNAOS tensor search optimizer.
"""

from __future__ import annotations

import random

from dl.models.optimization.tensor_candidate import (
    TensorCandidate,
)


class TensorSearchOptimizer:
    """
    Searches tensor optimization space.
    """

    def __init__(
        self,
        seed: int = 42,
    ) -> None:
        random.seed(
            seed,
        )

    def search(
        self,
        dimension: int,
        candidates: int,
    ) -> TensorCandidate:
        """
        Generate tensor candidates.
        """

        best_state = None
        best_score = float(
            "inf",
        )

        for _ in range(
            candidates,
        ):
            state = tuple(
                random.randint(
                    0,
                    1,
                )
                for _ in range(
                    dimension,
                )
            )

            score = sum(
                state,
            )

            if score < best_score:
                best_state = state
                best_score = score

        return TensorCandidate(
            state=best_state,
            score=best_score,
        )
