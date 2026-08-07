"""
RNA biological structure constraint validator.
"""

from __future__ import annotations


class RNAConstraintValidator:
    """
    Validates RNA secondary structures.
    """

    PAIRS = {
        ("A", "U"),
        ("U", "A"),
        ("G", "C"),
        ("C", "G"),
        ("G", "U"),
        ("U", "G"),
    }

    def validate(
        self,
        sequence: str,
        structure: str,
    ) -> bool:
        """
        Validate RNA secondary structure.
        """

        if len(sequence) != len(structure):
            return False

        stack: list[int] = []

        pairs: list[tuple[int, int]] = []

        for index, symbol in enumerate(structure):
            if symbol == "(":
                stack.append(index)

            elif symbol == ")":
                if not stack:
                    return False

                left = stack.pop()

                right = index

                pairs.append(
                    (
                        left,
                        right,
                    )
                )

                # Minimum hairpin loop size
                if right - left - 1 < 3:
                    return False

            elif symbol != ".":
                return False

        # Unbalanced brackets
        if stack:
            return False

        # Validate nucleotide pairing
        return all(
            (
                sequence[left],
                sequence[right],
            )
            in self.PAIRS
            for left, right in pairs
        )
