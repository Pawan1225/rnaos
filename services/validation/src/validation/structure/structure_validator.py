"""
RNA secondary structure validator.
"""

from __future__ import annotations


class StructureValidator:
    """
    Validates dot-bracket RNA structures.
    """

    def validate(
        self,
        structure: str,
    ) -> bool:
        """
        Check dot-bracket correctness.
        """

        balance = 0

        for symbol in structure:
            if symbol == "(":
                balance += 1

            elif symbol == ")":
                balance -= 1

                if balance < 0:
                    return False

            elif symbol != ".":
                return False

        return balance == 0
