"""
RNAOS feature engineering engine.
"""

from __future__ import annotations

from ai.models.feature_vector import (
    FeatureVector,
)
from ai.utils.normalization import (
    validate_features,
)
from biology.models.biological_intelligence_profile import (
    BiologicalIntelligenceProfile,
)


class FeatureEngineeringEngine:
    """
    Generate deterministic AI-ready feature vectors from
    biological intelligence profiles.

    Architecture
    ------------
    Converts biological intelligence into a deterministic
    numerical feature representation.

    Complexity
    ----------
    Time Complexity: O(1)

    The extractor performs constant-time aggregation over
    precomputed biological profiles.

    The extracted feature vector serves as the common input
    representation for downstream AI, machine learning,
    deep learning, quantum machine learning, and optimization
    engines.
    """

    DEFAULT_FEATURE_NAMES: tuple[str, ...] = (
        "sequence_length",
        "gc_content",
        "au_content",
        "gc_skew",
        "gc_au_ratio",
        "purine_pyrimidine_ratio",
        "entropy",
        "sequence_diversity",
        "repetition_score",
        "complexity_score",
        "estimated_stems",
        "estimated_loops",
        "average_stem_length",
        "average_loop_length",
        "gc_stability",
        "au_stability",
        "pair_density",
        "stem_stability",
        "stability_index",
        "approximate_free_energy",
        "gc_entropy_interaction",
        "stability_complexity_interaction",
    )

    def _extract_values(
        self,
        profile: BiologicalIntelligenceProfile,
    ) -> tuple[float, ...]:
        """
        Extract deterministic feature values.
        """
        return (
            float(profile.sequence.length),
            profile.gc_content.gc_content,
            profile.gc_content.au_content,
            profile.gc_content.gc_skew,
            profile.gc_content.gc_au_ratio,
            profile.gc_content.purine_pyrimidine_ratio,
            profile.complexity.entropy,
            profile.complexity.sequence_diversity,
            profile.complexity.repetition_score,
            profile.complexity.complexity_score,
            float(profile.stem_loops.estimated_stems),
            float(profile.stem_loops.estimated_loops),
            profile.stem_loops.average_stem_length,
            profile.stem_loops.average_loop_length,
            profile.thermodynamics.gc_stability,
            profile.thermodynamics.au_stability,
            profile.thermodynamics.pair_density,
            profile.thermodynamics.stem_stability,
            profile.thermodynamics.stability_index,
            profile.thermodynamics.approximate_free_energy,
            (profile.gc_content.gc_content * profile.complexity.entropy),
            (profile.thermodynamics.stability_index * profile.complexity.complexity_score),
        )

    def _build_vector(
        self,
        values: tuple[float, ...],
    ) -> FeatureVector:
        """
        Build a feature vector.
        """
        return FeatureVector(
            feature_names=self.DEFAULT_FEATURE_NAMES,
            values=values,
            dimension=len(values),
        )

    def extract(
        self,
        profile: BiologicalIntelligenceProfile,
    ) -> FeatureVector:
        """
        Extract an AI-ready feature vector.
        """
        values = self._extract_values(
            profile,
        )

        values = validate_features(
            values,
        )

        if len(values) != len(
            self.DEFAULT_FEATURE_NAMES,
        ):
            raise ValueError("Feature dimension mismatch.")

        return self._build_vector(
            values,
        )
