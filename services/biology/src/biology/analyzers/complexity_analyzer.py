"""
RNAOS complexity analyzer.
"""

from __future__ import annotations

import zlib

from biology.models.complexity_profile import (
    ComplexityProfile,
)
from biology.models.sequence_features import (
    SequenceFeatures,
)
from biology.utils.statistics import (
    normalize,
    nucleotide_diversity,
    probability_distribution,
    shannon_entropy,
)


class ComplexityAnalyzer:
    """
    Analyze RNA sequence complexity.
    """

    def analyze(
        self,
        features: SequenceFeatures,
    ) -> ComplexityProfile:
        """
        Analyze sequence complexity.
        """
        sequence = features.sequence

        probabilities = probability_distribution(
            features.nucleotide_counts.as_dict(),
        )

        entropy = shannon_entropy(
            probabilities,
        )

        sequence_diversity = nucleotide_diversity(
            sequence,
        )

        repetition_score = 1.0 - sequence_diversity

        compressed = zlib.compress(
            sequence.encode(),
        )

        compression_ratio = len(compressed) / max(
            len(sequence.encode()),
            1,
        )

        linguistic_complexity = normalize(
            sequence_diversity,
            0.0,
            1.0,
        )

        complexity_score = (
            entropy
            + sequence_diversity
            + linguistic_complexity
            + (1.0 - repetition_score)
            + (1.0 - compression_ratio)
        ) / 5.0

        return ComplexityProfile(
            entropy=entropy,
            sequence_diversity=sequence_diversity,
            repetition_score=repetition_score,
            linguistic_complexity=linguistic_complexity,
            compression_ratio=compression_ratio,
            complexity_score=complexity_score,
        )
