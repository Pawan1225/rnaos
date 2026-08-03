"""
RNA Folding Search Space.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from folding.basepairs import BasePairCandidate


@dataclass(slots=True)
class ConflictEdge:
    """
    Represents a conflict between two candidate base pairs.
    """

    first: int
    second: int
    reason: str


@dataclass(slots=True)
class FoldingSearchSpace:
    """
    Represents the complete RNA folding search space.
    """

    candidates: list[BasePairCandidate]

    conflicts: list[ConflictEdge] = field(default_factory=list)

    @property
    def variable_count(self) -> int:
        """
        Number of binary optimization variables.
        """
        return len(self.candidates)

    @property
    def conflict_count(self) -> int:
        """
        Number of pairwise conflicts.
        """
        return len(self.conflicts)

    @property
    def density(self) -> float:
        """
        Average conflicts per variable.
        """

        if not self.candidates:
            return 0.0

        return self.conflict_count / self.variable_count
