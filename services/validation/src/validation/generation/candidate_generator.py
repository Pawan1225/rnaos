"""
RNA candidate structure generator.
"""

from __future__ import annotations

from validation.generation.candidate_mutator import (
    CandidateMutator,
)


class CandidateGenerator:
    """
    Generates RNA secondary structure candidates.
    """

    def __init__(self) -> None:
        self.mutator = CandidateMutator()

    def generate(
        self,
        sequence: str,
    ) -> tuple[str, ...]:
        """
        Generate candidate structures.
        """

        length = len(sequence)

        base_candidates: list[str] = []

        # Fully unpaired structure
        base_candidates.append(
            "." * length,
        )

        # Simple paired structure
        if length >= 6:
            pair_size = min(
                3,
                length // 2,
            )

            middle = length - (pair_size * 2)

            base_candidates.append("(" * pair_size + "." * middle + ")" * pair_size)

        candidates: list[str] = []

        for structure in base_candidates:
            mutations = self.mutator.mutate(
                structure,
            )

            candidates.extend(
                mutations,
            )

        return tuple(
            dict.fromkeys(
                candidates,
            )
        )
