"""
RNA Folding Search Space Builder.
"""

from __future__ import annotations

from folding.basepairs import BasePairCandidate
from folding.search.search_space import (
    ConflictEdge,
    FoldingSearchSpace,
)


class SearchSpaceBuilder:
    """
    Build RNA folding search spaces from candidate base pairs.
    """

    def build(
        self,
        candidates: list[BasePairCandidate],
    ) -> FoldingSearchSpace:
        """
        Construct the folding search space and its conflict graph.
        """

        conflicts: list[ConflictEdge] = []

        for i, a in enumerate(candidates):
            for j in range(i + 1, len(candidates)):
                b = candidates[j]

                # --------------------------------------------------
                # Shared nucleotide conflict
                # --------------------------------------------------

                if a.left == b.left or a.left == b.right or a.right == b.left or a.right == b.right:
                    conflicts.append(
                        ConflictEdge(
                            first=i,
                            second=j,
                            reason="shared_nucleotide",
                        )
                    )
                    continue

                # --------------------------------------------------
                # Crossing pairs (pseudoknots not allowed)
                # --------------------------------------------------

                if a.left < b.left < a.right < b.right or b.left < a.left < b.right < a.right:
                    conflicts.append(
                        ConflictEdge(
                            first=i,
                            second=j,
                            reason="crossing_pair",
                        )
                    )

        return FoldingSearchSpace(
            candidates=candidates,
            conflicts=conflicts,
        )
