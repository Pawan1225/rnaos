"""
RNA Secondary Structure Model.

Defines the core biological data model used throughout the
RNA Folding Intelligence service.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class BasePair:
    """
    Represents a paired nucleotide.

    Attributes
    ----------
    left : int
        Index of the left nucleotide.
    right : int
        Index of the right nucleotide.
    """

    left: int
    right: int


@dataclass(slots=True)
class RNASecondaryStructure:
    """
    Represents an RNA secondary structure prediction.
    """

    sequence: str
    dot_bracket: str
    mfe: float

    base_pairs: list[BasePair] = field(default_factory=list)

    stems: list[list[BasePair]] = field(default_factory=list)

    hairpin_loops: list[list[int]] = field(default_factory=list)

    internal_loops: list[list[int]] = field(default_factory=list)

    bulges: list[list[int]] = field(default_factory=list)

    multiloops: list[list[int]] = field(default_factory=list)

    unpaired_positions: list[int] = field(default_factory=list)

    metadata: dict[str, str] = field(default_factory=dict)

    def __post_init__(self) -> None:
        """
        Validate the structure after initialization.
        """
        if len(self.sequence) != len(self.dot_bracket):
            raise ValueError("Sequence and dot-bracket notation must have the same length.")

    @property
    def length(self) -> int:
        """
        Length of the RNA sequence.
        """
        return len(self.sequence)

    @property
    def pair_count(self) -> int:
        """
        Number of base pairs.
        """
        return len(self.base_pairs)

    @property
    def num_base_pairs(self) -> int:
        """
        Alias for pair_count.

        Kept for compatibility with future modules.
        """
        return self.pair_count

    @property
    def is_folded(self) -> bool:
        """
        True if at least one base pair exists.
        """
        return self.pair_count > 0

    @property
    def is_unfolded(self) -> bool:
        """
        True if no base pairs exist.
        """
        return self.pair_count == 0
