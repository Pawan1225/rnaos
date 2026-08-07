"""
RNA base pair extraction utilities.
"""

from __future__ import annotations


class BasePairAnalyzer:
    """
    Extracts base pairs from dot bracket structures.
    """

    def extract(
        self,
        structure: str,
    ) -> tuple[tuple[int, int], ...]:
        """
        Extract paired positions.
        """

        stack: list[int] = []

        pairs: list[tuple[int, int]] = []

        for index, symbol in enumerate(
            structure,
        ):
            if symbol == "(":
                stack.append(index)

            elif symbol == ")":
                if not stack:
                    continue

                left = stack.pop()

                pairs.append(
                    (
                        left,
                        index,
                    )
                )

        return tuple(pairs)
