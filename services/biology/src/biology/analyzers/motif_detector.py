"""
RNAOS motif detector.
"""

from __future__ import annotations

from biology.models.motif_profile import MotifProfile
from biology.models.sequence_features import (
    SequenceFeatures,
)
from biology.utils.motif_library import (
    CANONICAL_START,
    CANONICAL_STOP,
)
from biology.utils.motif_search import find_motif


class MotifDetector:
    """
    Detect biologically relevant RNA motifs.
    """

    def analyze(
        self,
        features: SequenceFeatures,
    ) -> MotifProfile:
        """
        Detect motifs within an RNA sequence.
        """
        sequence = features.sequence

        canonical = tuple(
            find_motif(sequence, motif)
            for motif in (
                *CANONICAL_START,
                *CANONICAL_STOP,
            )
        )

        return MotifProfile(
            canonical=canonical,
            repetitive=(),
            structural=(),
            regulatory=(),
            custom=(),
        )
