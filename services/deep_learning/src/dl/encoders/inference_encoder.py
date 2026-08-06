"""
RNAOS inference sequence encoder.
"""

from __future__ import annotations


class InferenceSequenceEncoder:
    """
    Converts RNA sequences into numerical inputs.
    """

    _ENCODING = {
        "A": 0.0,
        "U": 1.0,
        "G": 2.0,
        "C": 3.0,
    }

    def encode(
        self,
        sequence: str,
    ) -> tuple[float, ...]:
        """
        Encode RNA sequence.
        """

        return tuple(self._ENCODING[nucleotide] for nucleotide in sequence)
