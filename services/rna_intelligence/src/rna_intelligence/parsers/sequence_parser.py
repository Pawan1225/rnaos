"""
RNA Sequence Parser

Responsible for converting raw RNA sequence input into a structured
RNASequence object used throughout RNAOS.
"""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass(slots=True)
class RNASequence:
    """Structured representation of an RNA sequence."""

    sequence: str
    length: int
    created_at: datetime = field(default_factory=datetime.utcnow)
    metadata: dict[str, str] = field(default_factory=dict)


class RNASequenceParser:
    """Parses raw RNA sequence input."""

    VALID_BASES = {"A", "U", "G", "C"}

    def parse(self, sequence: str) -> RNASequence:
        """
        Parse an RNA sequence.

        Parameters
        ----------
        sequence : str
            Raw RNA sequence.

        Returns
        -------
        RNASequence
        """

        if sequence is None:
            raise ValueError("Sequence cannot be None.")

        cleaned = sequence.strip().upper()

        if not cleaned:
            raise ValueError("Sequence cannot be empty.")

        return RNASequence(
            sequence=cleaned,
            length=len(cleaned),
        )
