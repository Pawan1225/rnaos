"""
RNAOS RNA structure encoder.
"""

from __future__ import annotations

from typing import ClassVar

from dl.core.base_encoder import (
    BaseEncoder,
)


class RNAStructureEncoder(BaseEncoder):
    """
    Encodes RNA secondary structure into
    neural tensor representations.
    """

    STRUCTURE_MAP: ClassVar[dict[str, tuple[float, ...]]] = {
        "(": (
            1.0,
            0.0,
        ),
        ")": (
            1.0,
            0.0,
        ),
        ".": (
            0.0,
            1.0,
        ),
    }

    def encode(
        self,
        inputs: str,
    ) -> tuple[tuple[float, ...], ...]:
        """
        Encode secondary structure.
        """

        return tuple(
            self.STRUCTURE_MAP.get(
                symbol,
                (
                    0.0,
                    0.0,
                ),
            )
            for symbol in inputs
        )

    def output_dimension(
        self,
    ) -> int:
        """
        Return structure encoding dimension.
        """

        return 2

    def save(
        self,
        path: str,
    ) -> None:
        """
        Structure encoder has no trainable parameters.
        """

        return None

    def load(
        self,
        path: str,
    ) -> None:
        """
        Structure encoder has no trainable parameters.
        """

        return None
