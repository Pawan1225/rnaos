"""
RNAOS foundation model interface.
"""

from __future__ import annotations

from dl.models.foundation_model import (
    FoundationModelInfo,
)


class RNAFoundationModelInterface:
    """
    Interface for RNA foundation models.
    """

    def __init__(
        self,
        info: FoundationModelInfo,
    ) -> None:
        self.info = info

    def encode(
        self,
        sequence: str,
    ) -> tuple[float, ...]:
        """
        Generate RNA representation.

        Placeholder for future
        foundation models.
        """

        return tuple(
            float(index)
            for index, _ in enumerate(
                sequence,
            )
        )
