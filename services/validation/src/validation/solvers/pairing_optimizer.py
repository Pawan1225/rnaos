"""
RNAOS pairing optimizer.

Generates RNA secondary structure
candidates using nucleotide pairing rules.
"""

from __future__ import annotations


class PairingOptimizer:
    """
    Simple RNA pairing optimizer.

    Uses classical base-pair rules:
    A-U
    G-C
    G-U
    """

    PAIRS = {
        ("A", "U"),
        ("U", "A"),
        ("G", "C"),
        ("C", "G"),
        ("G", "U"),
        ("U", "G"),
    }

    def can_pair(
        self,
        left: str,
        right: str,
    ) -> bool:
        """
        Check nucleotide compatibility.
        """

        return (
            left,
            right,
        ) in self.PAIRS

    def optimize(
        self,
        sequence: str,
    ) -> str:
        """
        Generate a paired RNA structure.
        """

        length = len(sequence)

        structure = ["." for _ in range(length)]

        left = 0
        right = length - 1

        while left < right:
            if self.can_pair(
                sequence[left],
                sequence[right],
            ):
                structure[left] = "("
                structure[right] = ")"

            left += 1
            right -= 1

        return "".join(structure)
