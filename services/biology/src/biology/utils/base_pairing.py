"""
RNAOS RNA base pairing utilities.
"""

from __future__ import annotations

BASE_PAIRS: dict[str, str] = {
    "A": "U",
    "U": "A",
    "G": "C",
    "C": "G",
}


def complement(
    nucleotide: str,
) -> str:
    """
    Return the complementary RNA nucleotide.

    Parameters
    ----------
    nucleotide
        RNA nucleotide.

    Returns
    -------
    str
        Complementary nucleotide, or an empty string if invalid.
    """
    return BASE_PAIRS.get(
        nucleotide,
        "",
    )


def is_complement(
    first: str,
    second: str,
) -> bool:
    """
    Check whether two nucleotides form a canonical RNA base pair.
    """
    return complement(first) == second


def reverse_complement(
    sequence: str,
) -> str:
    """
    Compute the reverse complement of an RNA sequence.
    """
    return "".join(complement(base) for base in reversed(sequence))


def pairing_score(
    first: str,
    second: str,
) -> float:
    """
    Compute a simple pairing score.

    Returns
    -------
    float
        1.0 for a canonical base pair, otherwise 0.0.
    """
    return 1.0 if is_complement(first, second) else 0.0


def complementarity(
    left: str,
    right: str,
) -> float:
    """
    Compute the complementarity score between two RNA sequences.

    The score is the fraction of complementary nucleotide pairs.

    Parameters
    ----------
    left
        First RNA sequence.

    right
        Second RNA sequence.

    Returns
    -------
    float
        Complementarity score in the range [0.0, 1.0].
    """
    if len(left) != len(right):
        raise ValueError("Sequences must have equal length.")

    if not left:
        return 0.0

    matches = sum(
        is_complement(a, b)
        for a, b in zip(
            left,
            right,
            strict=True,
        )
    )

    return matches / len(left)
