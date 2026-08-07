"""
RNAOS demo RNA input handler.
"""

from __future__ import annotations


class RNAInputHandler:
    """
    Validates RNA sequences for demo input.
    """

    VALID_BASES = frozenset("AUCG")

    def validate(
        self,
        sequence: str,
    ) -> str:
        """
        Normalize and validate RNA sequence.
        """

        normalized = sequence.strip().upper()

        if not normalized:
            raise ValueError("RNA sequence is empty")

        if not set(normalized).issubset(self.VALID_BASES):
            raise ValueError("Invalid RNA sequence")

        return normalized
