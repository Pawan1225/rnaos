"""
RNAOS thermodynamic utility functions.
"""

from __future__ import annotations

from biology.models.gc_content_features import (
    GCContentFeatures,
)
from biology.models.stem_loop_profile import (
    StemLoopProfile,
)


def gc_stability(
    gc_features: GCContentFeatures,
) -> float:
    """
    Estimate GC stability.

    Returns
    -------
    float
        Normalized GC stability score.
    """
    value = gc_features.gc_content

    return max(
        0.0,
        min(value, 1.0),
    )


def au_stability(
    gc_features: GCContentFeatures,
) -> float:
    """
    Estimate AU stability.

    Returns
    -------
    float
        Normalized AU stability score.
    """
    value = gc_features.au_content

    return max(
        0.0,
        min(value, 1.0),
    )


def pair_density(
    stem_profile: StemLoopProfile,
    sequence_length: int,
) -> float:
    """
    Estimate RNA base-pair density.

    Parameters
    ----------
    stem_profile
        Stem-loop profile.

    sequence_length
        RNA sequence length.

    Returns
    -------
    float
        Fraction of nucleotides participating in stems.
    """
    if sequence_length == 0:
        return 0.0

    paired = sum(2 * candidate.stem_length for candidate in stem_profile.candidates)

    value = paired / sequence_length

    return max(
        0.0,
        min(value, 1.0),
    )


def stem_stability(
    stem_profile: StemLoopProfile,
) -> float:
    """
    Estimate stability contributed by stem structures.

    Returns
    -------
    float
        Normalized stem stability score.
    """
    if stem_profile.estimated_stems == 0:
        return 0.0

    value = stem_profile.average_stem_length / 12.0

    return max(
        0.0,
        min(value, 1.0),
    )


def stability_index(
    gc_stability_score: float,
    stem_stability_score: float,
    pair_density_score: float,
) -> float:
    """
    Compute an overall stability index.

    Returns
    -------
    float
        Normalized stability index.
    """
    value = (gc_stability_score + stem_stability_score + pair_density_score) / 3.0

    return max(
        0.0,
        min(value, 1.0),
    )


def approximate_free_energy(
    gc_stability_score: float,
    stem_stability_score: float,
) -> float:
    """
    Estimate relative free energy.

    More negative values indicate greater predicted
    thermodynamic stability.

    Returns
    -------
    float
        Relative free-energy indicator.
    """
    return -10.0 * (0.7 * gc_stability_score + 0.3 * stem_stability_score)
