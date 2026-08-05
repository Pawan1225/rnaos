"""
RNAOS nucleotide count models.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class NucleotideCounts:
    """
    Canonical RNA nucleotide counts.
    """

    adenine: int

    uracil: int

    guanine: int

    cytosine: int

    @classmethod
    def from_counter(
        cls,
        counts: Counter[str],
    ) -> NucleotideCounts:
        """
        Construct nucleotide counts from a Counter.
        """
        return cls(
            adenine=counts["A"],
            uracil=counts["U"],
            guanine=counts["G"],
            cytosine=counts["C"],
        )

    @classmethod
    def from_dict(
        cls,
        counts: dict[str, int],
    ) -> NucleotideCounts:
        """
        Construct nucleotide counts from a dictionary.
        """
        return cls(
            adenine=counts.get("A", 0),
            uracil=counts.get("U", 0),
            guanine=counts.get("G", 0),
            cytosine=counts.get("C", 0),
        )

    @classmethod
    def from_sequence(
        cls,
        sequence: str,
    ) -> NucleotideCounts:
        """
        Construct nucleotide counts directly from an RNA sequence.
        """
        return cls.from_counter(
            Counter(sequence),
        )

    @property
    def total(self) -> int:
        """
        Total nucleotide count.
        """
        return self.adenine + self.uracil + self.guanine + self.cytosine

    @property
    def purine_count(self) -> int:
        """
        Number of purine nucleotides (A + G).
        """
        return self.adenine + self.guanine

    @property
    def pyrimidine_count(self) -> int:
        """
        Number of pyrimidine nucleotides (C + U).
        """
        return self.cytosine + self.uracil

    def as_dict(self) -> dict[str, int]:
        """
        Return nucleotide counts as a dictionary.
        """
        return {
            "A": self.adenine,
            "U": self.uracil,
            "G": self.guanine,
            "C": self.cytosine,
        }
