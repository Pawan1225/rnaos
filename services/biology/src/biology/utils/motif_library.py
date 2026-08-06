"""
RNAOS canonical motif definitions.
"""

from __future__ import annotations

# Canonical RNA translation motifs

CANONICAL_START: tuple[str, ...] = ("AUG",)

CANONICAL_STOP: tuple[str, ...] = (
    "UAA",
    "UAG",
    "UGA",
)

# Homopolymer motifs

POLY_A: tuple[str, ...] = ("AAAA",)

POLY_U: tuple[str, ...] = ("UUUU",)

POLY_G: tuple[str, ...] = ("GGGG",)

POLY_C: tuple[str, ...] = ("CCCC",)
