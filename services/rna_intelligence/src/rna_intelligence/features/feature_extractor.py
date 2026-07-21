"""
RNA Feature Extraction

Computes biologically meaningful features from RNA sequences.
"""

import math
from dataclasses import dataclass

from rna_intelligence.parsers.sequence_parser import RNASequence


@dataclass(slots=True)
class RNAFeatures:
    """Feature representation of an RNA sequence."""

    length: int
    base_counts: dict[str, int]
    gc_content: float
    au_content: float
    nucleotide_frequencies: dict[str, float]
    sequence_entropy: float


class FeatureExtractor:
    """Extracts biologically meaningful features from RNA sequences."""

    def extract(self, rna: RNASequence) -> RNAFeatures:
        """Extract features from an RNA sequence."""

        sequence = rna.sequence
        length = rna.length

        counts: dict[str, int] = {
            "A": sequence.count("A"),
            "U": sequence.count("U"),
            "G": sequence.count("G"),
            "C": sequence.count("C"),
        }

        gc_content = (counts["G"] + counts["C"]) / length
        au_content = (counts["A"] + counts["U"]) / length

        nucleotide_frequencies = {base: count / length for base, count in counts.items()}

        entropy = -sum(p * math.log2(p) for p in nucleotide_frequencies.values() if p > 0)

        return RNAFeatures(
            length=length,
            base_counts=counts,
            gc_content=gc_content,
            au_content=au_content,
            nucleotide_frequencies=nucleotide_frequencies,
            sequence_entropy=entropy,
        )
