"""
Combined RNA candidate generator.
"""

from __future__ import annotations

from validation.generation.multi_stem_generator import (
    MultiStemGenerator,
)
from validation.generation.pairing_candidate_generator import (
    PairingCandidateGenerator,
)


class CombinedCandidateGenerator:
    """
    Combines multiple RNA candidate strategies.
    """

    def __init__(self) -> None:

        self.pairing_generator = PairingCandidateGenerator()

        self.multi_stem_generator = MultiStemGenerator()

    def generate(
        self,
        sequence: str,
    ) -> tuple[str, ...]:
        """
        Generate combined candidates.
        """

        candidates = []

        candidates.extend(
            self.pairing_generator.generate(
                sequence,
            )
        )

        candidates.extend(
            self.multi_stem_generator.generate(
                sequence,
            )
        )

        return tuple(
            dict.fromkeys(
                candidates,
            )
        )
