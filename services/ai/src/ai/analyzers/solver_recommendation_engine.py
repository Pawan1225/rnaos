"""
RNAOS solver recommendation engine.
"""

from __future__ import annotations

from ai.models.meta_feature_profile import (
    MetaFeatureProfile,
)
from ai.models.solver_recommendation_features import (
    SolverRecommendationFeatures,
)
from ai.utils.solver_scoring import (
    affinity_score,
    clamp,
    confidence_score,
    runtime_score,
)
from biology.models.biological_intelligence_profile import (
    BiologicalIntelligenceProfile,
)


class SolverRecommendationEngine:
    """
    Generate deterministic solver recommendation features.

    Architecture
    ------------
    Converts biological intelligence and AI meta features
    into optimization recommendation features suitable for
    downstream optimization engines.

    Complexity
    ----------
    Time Complexity: O(1)
    """

    def analyze(
        self,
        profile: BiologicalIntelligenceProfile,
        meta_features: MetaFeatureProfile,
    ) -> SolverRecommendationFeatures:
        """
        Generate solver recommendation features.
        """
        sequence_length = max(
            profile.sequence.length,
            1,
        )

        optimization_difficulty = clamp(
            (meta_features.optimization_complexity + meta_features.folding_difficulty) / 2.0,
        )

        search_space_complexity = clamp(
            (meta_features.structural_complexity + sequence_length / 1000.0) / 2.0,
        )

        constraint_density = clamp(
            (len(profile.motifs.canonical) + profile.stem_loops.estimated_stems) / sequence_length,
        )

        expected_runtime = runtime_score(
            optimization_difficulty=optimization_difficulty,
            search_space_complexity=search_space_complexity,
        )

        quantum_affinity = affinity_score(
            complexity=meta_features.optimization_complexity,
            stability=profile.thermodynamics.stability_index,
            quantum_suitability=meta_features.quantum_suitability,
        )

        classical_affinity = clamp(
            1.0 - quantum_affinity,
        )

        hybrid_affinity = clamp(
            (classical_affinity + quantum_affinity) / 2.0,
        )

        recommendation_confidence = confidence_score(
            classical=classical_affinity,
            quantum=quantum_affinity,
            hybrid=hybrid_affinity,
        )

        return SolverRecommendationFeatures(
            optimization_difficulty=optimization_difficulty,
            search_space_complexity=search_space_complexity,
            constraint_density=constraint_density,
            expected_runtime=expected_runtime,
            classical_affinity=classical_affinity,
            quantum_affinity=quantum_affinity,
            hybrid_affinity=hybrid_affinity,
            recommendation_confidence=recommendation_confidence,
        )
