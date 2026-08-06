"""
RNAOS explainable AI utilities.
"""

from __future__ import annotations

from ai.models.meta_feature_profile import (
    MetaFeatureProfile,
)
from ai.models.solver_recommendation_features import (
    SolverRecommendationFeatures,
)
from biology.models.biological_intelligence_profile import (
    BiologicalIntelligenceProfile,
)


def determine_strategy(
    recommendation: SolverRecommendationFeatures,
) -> str:
    """
    Determine the recommended optimization strategy.
    """
    affinities = {
        "Classical Optimization": recommendation.classical_affinity,
        "Quantum Optimization": recommendation.quantum_affinity,
        "Hybrid Optimization": recommendation.hybrid_affinity,
    }

    return max(
        affinities,
        key=affinities.get,
    )


def biological_factors(
    profile: BiologicalIntelligenceProfile,
) -> tuple[str, ...]:
    """
    Extract biological factors influencing optimization.
    """
    factors: list[str] = []

    if profile.gc_content.gc_content >= 0.6:
        factors.append(
            "High GC content",
        )

    if profile.stem_loops.estimated_stems > 0:
        factors.append(
            "Stem-loop structures detected",
        )

    if profile.complexity.complexity_score >= 0.5:
        factors.append(
            "Elevated sequence complexity",
        )

    if not factors:
        factors.append(
            "Typical biological characteristics",
        )

    return tuple(
        factors,
    )


def ai_factors(
    meta_features: MetaFeatureProfile,
) -> tuple[str, ...]:
    """
    Extract AI-derived reasoning factors.
    """
    factors: list[str] = []

    if meta_features.quantum_suitability >= 0.6:
        factors.append(
            "High quantum suitability",
        )

    if meta_features.optimization_complexity >= 0.5:
        factors.append(
            "Moderate optimization complexity",
        )

    if meta_features.ai_readiness_score >= 0.6:
        factors.append(
            "High AI readiness",
        )

    if not factors:
        factors.append(
            "Balanced AI characteristics",
        )

    return tuple(
        factors,
    )


def recommendation_summary(
    strategy: str,
) -> str:
    """
    Generate a concise recommendation summary.
    """
    return f"{strategy} is recommended based on the biological and AI analysis."


def technical_summary(
    profile: BiologicalIntelligenceProfile,
    meta_features: MetaFeatureProfile,
    recommendation: SolverRecommendationFeatures,
) -> str:
    """
    Generate a technical explanation.
    """
    return (
        "Recommendation generated using deterministic "
        f"analysis of a sequence length of "
        f"{profile.sequence.length}, "
        f"optimization complexity "
        f"{meta_features.optimization_complexity:.2f}, "
        f"and recommendation confidence "
        f"{recommendation.recommendation_confidence:.2f}."
    )
