"""
RNA multi-stem candidate generator.
"""

from __future__ import annotations


class MultiStemGenerator:
    """
    Generates structures containing
    multiple RNA stems.
    """

    PAIRS = {
        ("A", "U"),
        ("U", "A"),
        ("G", "C"),
        ("C", "G"),
        ("G", "U"),
        ("U", "G"),
    }

    MIN_STEM = 3

    def _can_pair(
        self,
        left: str,
        right: str,
    ) -> bool:
        return (
            left,
            right,
        ) in self.PAIRS

    def generate(
        self,
        sequence: str,
    ) -> tuple[str, ...]:
        """
        Generate multi-stem candidates.
        """

        length = len(sequence)

        candidates = ["." * length]

        for stem in range(
            self.MIN_STEM,
            min(4, length // 2) + 1,
        ):
            left = sequence[:stem]

            right = sequence[-stem:]

            valid = True

            for i in range(stem):
                if not self._can_pair(
                    left[i],
                    right[stem - i - 1],
                ):
                    valid = False
                    break

            if not valid:
                continue

            loop = length - (2 * stem)

            structure = "(" * stem + "." * loop + ")" * stem

            candidates.append(structure)

        return tuple(dict.fromkeys(candidates))
