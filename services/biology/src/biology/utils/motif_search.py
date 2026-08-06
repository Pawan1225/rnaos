"""
RNAOS motif search utilities.
"""

from __future__ import annotations

from biology.models.motif_occurrence import (
    MotifOccurrence,
)


def find_motif(
    sequence: str,
    motif: str,
) -> MotifOccurrence:
    """
    Find all occurrences of a motif within a sequence.

    Parameters
    ----------
    sequence
        RNA sequence.

    motif
        RNA motif.

    Returns
    -------
    MotifOccurrence
        Motif occurrence information.
    """
    positions: list[int] = []

    start = 0

    while True:
        index = sequence.find(
            motif,
            start,
        )

        if index == -1:
            break

        positions.append(index)

        start = index + 1

    return MotifOccurrence(
        motif=motif,
        count=len(positions),
        positions=tuple(positions),
    )
