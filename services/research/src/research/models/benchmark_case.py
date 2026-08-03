from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

VALID_BASES = {"A", "U", "G", "C"}


@dataclass(frozen=True, slots=True)
class BenchmarkCase:
    """
    Represents a single RNA benchmark sequence used for evaluation.

    Attributes
    ----------
    sequence_id:
        Unique identifier for the benchmark.
    sequence:
        RNA sequence.
    source:
        Dataset source (RNA STRAND, ArchiveII, Synthetic, etc.).
    reference_structure:
        Known secondary structure in dot-bracket notation.
    reference_energy:
        Reference free energy (kcal/mol).
    family:
        RNA family or category.
    metadata:
        Additional dataset-specific metadata.
    """

    sequence_id: str
    sequence: str
    source: str = "synthetic"
    reference_structure: str | None = None
    reference_energy: float | None = None
    family: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        sequence = self.sequence.upper()

        if not sequence:
            raise ValueError("RNA sequence cannot be empty.")

        invalid = set(sequence) - VALID_BASES
        if invalid:
            raise ValueError(f"Invalid RNA bases: {sorted(invalid)}")

        object.__setattr__(self, "sequence", sequence)

    @property
    def length(self) -> int:
        """Sequence length."""
        return len(self.sequence)

    @property
    def gc_content(self) -> float:
        """Fraction of G/C nucleotides."""
        gc = sum(base in {"G", "C"} for base in self.sequence)
        return gc / self.length
