"""
RNAOS stem-loop detector.
"""

from __future__ import annotations

from biology.models.sequence_features import (
    SequenceFeatures,
)
from biology.models.stem_loop_candidate import (
    StemLoopCandidate,
)
from biology.models.stem_loop_profile import (
    StemLoopProfile,
)
from biology.utils.base_pairing import (
    complementarity,
)


class StemLoopDetector:
    """
    Heuristic RNA stem-loop detector.

    Algorithm Complexity
    --------------------
    Worst-case time complexity: O(n³)

    The implementation favors deterministic and explainable
    heuristics over exhaustive RNA secondary-structure
    prediction. ViennaRNA remains the reference folding engine.

    The detector searches for complementary sequence regions that
    may form stem-loop (hairpin) structures. It intentionally
    provides fast, deterministic structural features rather than
    full secondary-structure prediction.
    """

    def __init__(
        self,
        *,
        min_stem_length: int = 3,
        min_loop_length: int = 3,
        max_loop_length: int = 8,
    ) -> None:
        self._min_stem_length = min_stem_length
        self._min_loop_length = min_loop_length
        self._max_loop_length = max_loop_length

    @property
    def min_stem_length(self) -> int:
        """
        Minimum stem length considered during detection.
        """
        return self._min_stem_length

    @property
    def min_loop_length(self) -> int:
        """
        Minimum loop length considered during detection.
        """
        return self._min_loop_length

    @property
    def max_loop_length(self) -> int:
        """
        Maximum loop length considered during detection.
        """
        return self._max_loop_length

    def _build_candidate(
        self,
        *,
        stem_start: int,
        stem_length: int,
        loop_length: int,
        score: float,
    ) -> StemLoopCandidate:
        """
        Build a stem-loop candidate.
        """
        right_start = stem_start + stem_length + loop_length

        return StemLoopCandidate(
            stem_start=stem_start,
            stem_end=stem_start + stem_length - 1,
            loop_start=stem_start + stem_length,
            loop_end=right_start - 1,
            stem_length=stem_length,
            loop_length=loop_length,
            score=score,
        )

    def _build_profile(
        self,
        candidates: list[StemLoopCandidate],
    ) -> StemLoopProfile:
        """
        Build a stem-loop profile.
        """
        if candidates:
            average_stem = sum(candidate.stem_length for candidate in candidates) / len(candidates)

            average_loop = sum(candidate.loop_length for candidate in candidates) / len(candidates)
        else:
            average_stem = 0.0
            average_loop = 0.0

        return StemLoopProfile(
            candidates=tuple(candidates),
            estimated_stems=len(candidates),
            estimated_loops=len(candidates),
            average_stem_length=average_stem,
            average_loop_length=average_loop,
        )

    def analyze(
        self,
        features: SequenceFeatures,
    ) -> StemLoopProfile:
        """
        Analyze an RNA sequence for candidate stem-loop structures.
        """
        sequence = features.sequence

        candidates: list[StemLoopCandidate] = []

        n = len(sequence)

        for stem_start in range(n):
            minimum_required = 2 * self._min_stem_length + self._min_loop_length

            remaining = n - stem_start

            if remaining < minimum_required:
                break

            max_stem_length = min(
                12,
                (n - stem_start) // 2,
            )

            for stem_length in range(
                self._min_stem_length,
                max_stem_length + 1,
            ):
                left = sequence[stem_start : stem_start + stem_length]

                for loop_length in range(
                    self._min_loop_length,
                    self._max_loop_length + 1,
                ):
                    right_start = stem_start + stem_length + loop_length

                    right_end = right_start + stem_length

                    if right_end > n:
                        continue

                    right = sequence[right_start:right_end]

                    score = complementarity(
                        left,
                        right[::-1],
                    )

                    if score < 1.0:
                        continue

                    candidates.append(
                        self._build_candidate(
                            stem_start=stem_start,
                            stem_length=stem_length,
                            loop_length=loop_length,
                            score=score,
                        )
                    )

        return self._build_profile(
            candidates,
        )
