"""
RNAOS statistical utilities.
"""

from __future__ import annotations

import math
from collections import Counter
from collections.abc import Iterable


def shannon_entropy(
    probabilities: Iterable[float],
) -> float:
    """
    Compute Shannon entropy.

    Parameters
    ----------
    probabilities
        Probability distribution.

    Returns
    -------
    float
        Shannon entropy in bits.
    """
    entropy = 0.0

    for probability in probabilities:
        if probability > 0:
            entropy -= probability * math.log2(
                probability,
            )

    return entropy


def normalize(
    value: float,
    minimum: float,
    maximum: float,
) -> float:
    """
    Normalize a value into the range [0, 1].
    """
    if maximum <= minimum:
        return 0.0

    return (value - minimum) / (maximum - minimum)


def probability_distribution(
    counts: Counter[str],
) -> tuple[float, ...]:
    """
    Convert counts into a probability distribution.
    """
    total = sum(
        counts.values(),
    )

    if total == 0:
        return ()

    return tuple(count / total for count in counts.values())


def unique_fraction(
    items: Iterable[object],
) -> float:
    """
    Fraction of unique values.
    """
    items = tuple(items)

    if not items:
        return 0.0

    return len(
        set(items),
    ) / len(items)


def nucleotide_diversity(
    sequence: str,
) -> float:
    """
    Compute nucleotide diversity.

    Defined as the fraction of the four canonical RNA
    nucleotides (A, U, G, C) present in the sequence.

    Returns
    -------
    float
        Diversity in the range [0.0, 1.0].
    """
    if not sequence:
        return 0.0

    return len(set(sequence)) / 4.0
