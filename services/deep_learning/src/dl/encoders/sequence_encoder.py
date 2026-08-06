"""
RNAOS RNA sequence encoder.
"""

from __future__ import annotations

from typing import ClassVar

from dl.core.base_encoder import (
    BaseEncoder,
)


class RNASequenceEncoder(BaseEncoder):
    """
    Encodes RNA nucleotide sequences into
    neural tensor representations.
    """

    NUCLEOTIDE_MAP: ClassVar[dict[str, tuple[float, ...]]] = {
        "A": (1.0, 0.0, 0.0, 0.0),
        "U": (0.0, 1.0, 0.0, 0.0),
        "G": (0.0, 0.0, 1.0, 0.0),
        "C": (0.0, 0.0, 0.0, 1.0),
    }

    def encode(
        self,
        inputs: str,
    ) -> tuple[tuple[float, ...], ...]:
        """
        Encode RNA sequence using one-hot encoding.
        """

        return tuple(
            self.NUCLEOTIDE_MAP.get(
                nucleotide,
                (
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                ),
            )
            for nucleotide in inputs.upper()
        )

    def output_dimension(
        self,
    ) -> int:
        """
        Return embedding input dimension.
        """

        return 4

    def save(
        self,
        path: str,
    ) -> None:
        """
        Sequence encoder has no trainable parameters.
        """

        return None

    def load(
        self,
        path: str,
    ) -> None:
        """
        Sequence encoder has no trainable parameters.
        """

        return None
