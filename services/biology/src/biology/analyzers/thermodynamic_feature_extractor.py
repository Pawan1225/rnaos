"""
RNAOS thermodynamic feature extractor.
"""

from __future__ import annotations

from biology.models.gc_content_features import (
    GCContentFeatures,
)
from biology.models.sequence_features import (
    SequenceFeatures,
)
from biology.models.stem_loop_profile import (
    StemLoopProfile,
)
from biology.models.thermodynamic_profile import (
    ThermodynamicProfile,
)
from biology.utils.thermodynamics import (
    approximate_free_energy,
    au_stability,
    gc_stability,
    pair_density,
    stability_index,
    stem_stability,
)


class ThermodynamicFeatureExtractor:
    """
    Extract deterministic thermodynamic features from RNA sequences.

    Algorithm Notes
    ---------------
    This module computes deterministic heuristic
    thermodynamic descriptors.

    The values are intended for downstream AI,
    machine learning, deep learning and optimization
    modules and are not substitutes for
    thermodynamic folding engines such as ViennaRNA.

    This module provides lightweight heuristic
    thermodynamic descriptors that complement
    structural analyses. These features are intended
    for downstream AI, ML, DL, and optimization
    modules rather than replacing full
    thermodynamic folding engines.
    """

    def _build_profile(
        self,
        *,
        gc_score: float,
        au_score: float,
        density: float,
        stem_score: float,
        stability: float,
        free_energy: float,
    ) -> ThermodynamicProfile:
        """
        Build a thermodynamic profile.
        """
        return ThermodynamicProfile(
            gc_stability=gc_score,
            au_stability=au_score,
            pair_density=density,
            stem_stability=stem_score,
            stability_index=stability,
            approximate_free_energy=free_energy,
        )

    def analyze(
        self,
        sequence_features: SequenceFeatures,
        gc_features: GCContentFeatures,
        stem_profile: StemLoopProfile,
    ) -> ThermodynamicProfile:
        """
        Extract thermodynamic features.
        """
        gc_score = gc_stability(
            gc_features,
        )

        au_score = au_stability(
            gc_features,
        )

        density = pair_density(
            stem_profile,
            len(sequence_features.sequence),
        )

        stem_score = stem_stability(
            stem_profile,
        )

        stability = stability_index(
            gc_score,
            stem_score,
            density,
        )

        free_energy = approximate_free_energy(
            gc_score,
            stem_score,
        )

        return self._build_profile(
            gc_score=gc_score,
            au_score=au_score,
            density=density,
            stem_score=stem_score,
            stability=stability,
            free_energy=free_energy,
        )
