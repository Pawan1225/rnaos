"""
RNAOS intelligence aggregation engine.
"""

from __future__ import annotations

from dl.models.optimization.intelligence_aggregation import (
    IntelligenceAggregation,
)
from dl.models.optimization.learning_profile import (
    LearningProfile,
)
from dl.models.optimization.meta_intelligence_profile import (
    MetaIntelligenceProfile,
)
from dl.models.optimization.solver_capability import (
    SolverCapability,
)


class IntelligenceAggregationEngine:
    """
    Aggregates optimization intelligence.
    """

    def aggregate(
        self,
        capabilities: tuple[
            SolverCapability,
            ...,
        ],
        learning_profile: LearningProfile,
        meta_profile: MetaIntelligenceProfile,
    ) -> IntelligenceAggregation:
        """
        Aggregate optimization intelligence.
        """

        if not capabilities:
            raise ValueError(
                "Capabilities cannot be empty",
            )

        total_values = sum(len(capability.capabilities) for capability in capabilities)

        capability_sum = sum(sum(capability.capabilities) for capability in capabilities)

        average_capability = capability_sum / total_values

        unified_score = (
            average_capability + learning_profile.confidence + meta_profile.confidence
        ) / 3.0

        return IntelligenceAggregation(
            total_features=total_values,
            average_capability=average_capability,
            learning_confidence=(learning_profile.confidence),
            meta_confidence=(meta_profile.confidence),
            unified_score=unified_score,
        )
