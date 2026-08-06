"""
RNAOS meta feature engine.
"""

from __future__ import annotations

from ai.models.meta_feature_profile import (
    MetaFeatureProfile,
)
from ai.utils.meta_feature_math import (
    clamp,
    complexity_score,
    interaction_score,
    readiness_score,
)
from biology.models.biological_intelligence_profile import (
    BiologicalIntelligenceProfile,
)


class MetaFeatureEngine:
    """
    Generate higher-order AI features from biological
    intelligence.

    Architecture
    ------------
    Converts biological intelligence into composite
    AI-oriented features suitable for downstream
    optimization and solver recommendation.

    Complexity
    ----------
    Time Complexity: O(1)
    """

    def analyze(
        self,
        profile: BiologicalIntelligenceProfile,
    ) -> MetaFeatureProfile:
        """
        Generate meta features from a biological profile.
        """
        sequence_length = max(
            profile.sequence.length,
            1,
        )

        stem_density = profile.stem_loops.estimated_stems / sequence_length

        motif_density = (
            len(
                profile.motifs.canonical,
            )
            / sequence_length
        )

        structural_complexity = complexity_score(
            complexity=profile.complexity.complexity_score,
            stem_density=stem_density,
            motif_density=motif_density,
        )

        folding_difficulty = interaction_score(
            profile.thermodynamics.stability_index,
            structural_complexity,
        )

        optimization_complexity = interaction_score(
            profile.complexity.complexity_score,
            structural_complexity,
        )

        stability_complexity_index = interaction_score(
            profile.thermodynamics.stability_index,
            profile.complexity.complexity_score,
        )

        quantum_suitability = clamp(
            (structural_complexity + profile.gc_content.gc_content) / 2.0,
        )

        ai_readiness = readiness_score(
            stability=profile.thermodynamics.stability_index,
            complexity=structural_complexity,
            quantum_suitability=quantum_suitability,
        )

        return MetaFeatureProfile(
            folding_difficulty=folding_difficulty,
            structural_complexity=structural_complexity,
            optimization_complexity=optimization_complexity,
            stability_complexity_index=stability_complexity_index,
            quantum_suitability=quantum_suitability,
            ai_readiness_score=ai_readiness,
        )
