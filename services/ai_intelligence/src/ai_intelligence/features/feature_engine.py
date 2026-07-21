"""
AI Feature Engineering Engine

Transforms RNAProfile objects into deterministic numerical feature vectors.
"""

from __future__ import annotations

from dataclasses import dataclass

from rna_intelligence.profilers.rna_profiler import RNAProfile


@dataclass(slots=True)
class FeatureVector:
    """Numerical feature vector for AI models."""

    values: list[float]
    feature_names: list[str]

    @property
    def dimension(self) -> int:
        """Return the dimensionality of the feature vector."""
        return len(self.values)


class FeatureEngineeringEngine:
    """Transforms RNA profiles into deterministic feature vectors."""

    FEATURE_NAMES = [
        "length",
        "gc_content",
        "au_content",
        "frequency_a",
        "frequency_u",
        "frequency_g",
        "frequency_c",
        "sequence_entropy",
    ]

    def transform(self, profile: RNAProfile) -> FeatureVector:
        """Generate a feature vector from an RNA profile."""

        features = profile.features

        values = [
            float(features.length),
            float(features.gc_content),
            float(features.au_content),
            float(features.nucleotide_frequencies["A"]),
            float(features.nucleotide_frequencies["U"]),
            float(features.nucleotide_frequencies["G"]),
            float(features.nucleotide_frequencies["C"]),
            float(features.sequence_entropy),
        ]

        return FeatureVector(
            values=values,
            feature_names=self.FEATURE_NAMES.copy(),
        )
