"""
RNA biological stem candidate generator.
"""

from __future__ import annotations


class PairingCandidateGenerator:
    """
    Generates RNA secondary structure candidates
    using complementary regions.
    """

    PAIRS = {
        ("A", "U"),
        ("U", "A"),
        ("G", "C"),
        ("C", "G"),
        ("G", "U"),
        ("U", "G"),
    }

    MIN_STEM_LENGTH = 3

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
        Generate candidate structures.
        """

        length = len(sequence)

        candidates = ["." * length]

        for stem_length in range(
            self.MIN_STEM_LENGTH,
            min(6, length // 2) + 1,
        ):
            for left_start in range(length - (2 * stem_length) + 1):
                left = sequence[left_start : left_start + stem_length]

                for right_start in range(
                    left_start + stem_length,
                    length - stem_length + 1,
                ):
                    right = sequence[right_start : right_start + stem_length]

                    valid = True

                    for i in range(stem_length):
                        if not self._can_pair(
                            left[i],
                            right[stem_length - i - 1],
                        ):
                            valid = False
                            break

                    if not valid:
                        continue

                    loop_length = right_start - (left_start + stem_length)

                    structure = (
                        "." * left_start
                        + "(" * stem_length
                        + "." * loop_length
                        + ")" * stem_length
                        + "." * (length - right_start - stem_length)
                    )

                    if len(structure) == length:
                        candidates.append(structure)

        return tuple(dict.fromkeys(candidates))
