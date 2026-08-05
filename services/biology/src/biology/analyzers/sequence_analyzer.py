"""
RNAOS sequence analyzer.
"""

from __future__ import annotations

from biology.models.nucleotide_counts import (
    NucleotideCounts,
)
from biology.models.sequence_features import (
    SequenceFeatures,
)
from biology.utils.sequence_validation import (
    normalize_sequence,
    validate_sequence,
)


class SequenceAnalyzer:
    """
    Analyze fundamental properties of an RNA sequence.
    """

    def analyze(
        self,
        sequence: str,
    ) -> SequenceFeatures:
        """
        Analyze an RNA sequence.

        Parameters
        ----------
        sequence
            Raw RNA sequence.

        Returns
        -------
        SequenceFeatures
            Fundamental sequence statistics.
        """
        normalized = normalize_sequence(sequence)

        validate_sequence(normalized)

        nucleotide_counts = NucleotideCounts.from_sequence(
            normalized,
        )

        return SequenceFeatures(
            sequence=normalized,
            length=nucleotide_counts.total,
            nucleotide_counts=nucleotide_counts,
            purine_count=nucleotide_counts.purine_count,
            pyrimidine_count=nucleotide_counts.pyrimidine_count,
            is_valid=True,
        )
