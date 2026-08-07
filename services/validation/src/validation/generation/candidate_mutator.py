"""
RNA candidate structure mutation engine.
"""

from __future__ import annotations


class CandidateMutator:
    """
    Generates structural variations
    from a base RNA structure.
    """

    def mutate(
        self,
        structure: str,
    ) -> tuple[str, ...]:
        """
        Generate candidate mutations.
        """

        candidates: list[str] = []

        length = len(structure)

        # Original structure
        candidates.append(
            structure,
        )

        # Shift structure right
        if "(" in structure and ")" in structure:
            shifted = "." + structure[:-1]

            candidates.append(
                shifted,
            )

        # Shift structure left
        if "(" in structure and ")" in structure:
            shifted = structure[1:] + "."

            candidates.append(
                shifted,
            )

        # Unpaired fallback
        candidates.append(
            "." * length,
        )

        return tuple(
            dict.fromkeys(
                candidates,
            )
        )
