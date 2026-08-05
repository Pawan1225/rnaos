"""
RNAOS biological constants.

This module defines canonical biological constants used throughout the
Biological Intelligence Framework.
"""

from __future__ import annotations

# ---------------------------------------------------------------------
# Canonical RNA nucleotides
# ---------------------------------------------------------------------

RNA_NUCLEOTIDES: frozenset[str] = frozenset(
    {
        "A",
        "U",
        "G",
        "C",
    }
)

# ---------------------------------------------------------------------
# Purines / Pyrimidines
# ---------------------------------------------------------------------

PURINES: frozenset[str] = frozenset(
    {
        "A",
        "G",
    }
)

PYRIMIDINES: frozenset[str] = frozenset(
    {
        "C",
        "U",
    }
)

# ---------------------------------------------------------------------
# Watson-Crick base pairing
# ---------------------------------------------------------------------

COMPLEMENTARY_BASES: dict[str, str] = {
    "A": "U",
    "U": "A",
    "G": "C",
    "C": "G",
}

# ---------------------------------------------------------------------
# Canonical nucleotide ordering
# ---------------------------------------------------------------------

NUCLEOTIDE_ORDER: tuple[str, ...] = (
    "A",
    "U",
    "G",
    "C",
)

# ---------------------------------------------------------------------
# Default motif length limits
# ---------------------------------------------------------------------

MIN_MOTIF_LENGTH: int = 3

MAX_MOTIF_LENGTH: int = 12

# ---------------------------------------------------------------------
# Default biological thresholds
# ---------------------------------------------------------------------

HIGH_GC_THRESHOLD: float = 0.60

LOW_GC_THRESHOLD: float = 0.40

HIGH_AU_THRESHOLD: float = 0.60

LOW_AU_THRESHOLD: float = 0.40
