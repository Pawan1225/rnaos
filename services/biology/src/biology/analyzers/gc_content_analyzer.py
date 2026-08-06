"""
RNAOS GC content analyzer.
"""

from __future__ import annotations

from biology.models.gc_content_features import (
    GCContentFeatures,
)
from biology.models.sequence_features import (
    SequenceFeatures,
)


class GCContentAnalyzer:
    """
    Analyze nucleotide composition statistics for an RNA sequence.
    """

    @staticmethod
    def _safe_divide(
        numerator: float,
        denominator: float,
    ) -> float:
        """
        Safely divide two values.

        Returns 0.0 if the denominator is zero.
        """
        if denominator == 0:
            return 0.0

        return numerator / denominator

    def analyze(
        self,
        features: SequenceFeatures,
    ) -> GCContentFeatures:
        """
        Analyze GC composition statistics.

        Parameters
        ----------
        features
            Sequence features produced by the SequenceAnalyzer.

        Returns
        -------
        GCContentFeatures
            GC composition statistics.
        """
        counts = features.nucleotide_counts

        gc = counts.guanine + counts.cytosine

        au = counts.adenine + counts.uracil

        purines = counts.purine_count

        pyrimidines = counts.pyrimidine_count

        total = counts.total

        return GCContentFeatures(
            gc_content=self._safe_divide(
                gc,
                total,
            ),
            au_content=self._safe_divide(
                au,
                total,
            ),
            gc_skew=self._safe_divide(
                counts.guanine - counts.cytosine,
                gc,
            ),
            gc_au_ratio=self._safe_divide(
                gc,
                au,
            ),
            purine_pyrimidine_ratio=self._safe_divide(
                purines,
                pyrimidines,
            ),
        )
