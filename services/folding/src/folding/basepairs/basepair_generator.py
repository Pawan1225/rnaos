"""
Base Pair Generator.

Generates biologically valid RNA base-pair candidates.
"""

from __future__ import annotations

from dataclasses import dataclass

_ALLOWED = {
    ("A", "U"),
    ("U", "A"),
    ("G", "C"),
    ("C", "G"),
    ("G", "U"),
    ("U", "G"),
}


@dataclass(slots=True)
class BasePairCandidate:
    """
    Represents a candidate RNA base pair.
    """

    left: int
    right: int

    left_base: str
    right_base: str

    @property
    def distance(self) -> int:
        """
        Distance between paired nucleotides.
        """
        return self.right - self.left

    @property
    def pair_type(self) -> str:
        """
        Return the nucleotide pair type.
        """
        return f"{self.left_base}-{self.right_base}"


class BasePairGenerator:
    """
    Generate biologically valid RNA base pairs.
    """

    def __init__(
        self,
        minimum_loop_length: int = 4,
    ) -> None:
        self.minimum_loop_length = minimum_loop_length

    def generate(
        self,
        sequence: str,
    ) -> list[BasePairCandidate]:
        """
        Generate all biologically valid base-pair candidates.
        """

        candidates: list[BasePairCandidate] = []

        n = len(sequence)

        for i in range(n):
            for j in range(
                i + self.minimum_loop_length,
                n,
            ):
                pair = (
                    sequence[i],
                    sequence[j],
                )

                if pair in _ALLOWED:
                    candidates.append(
                        BasePairCandidate(
                            left=i,
                            right=j,
                            left_base=sequence[i],
                            right_base=sequence[j],
                        )
                    )

        return candidates
