from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field

from decision.models.decision_reason import DecisionReason


class Explanation(BaseModel):
    """
    Complete explanation for a decision produced by RNAOS.

    An Explanation represents the final explainable output returned by
    the Decision Intelligence layer. It combines the recommended action,
    supporting reasons, confidence score, alternative options, trade-offs,
    and additional metadata into a single structured object.

    This model is intentionally domain-agnostic and can be reused for
    explaining solver selection, optimization formulation, RNA folding,
    benchmarking results, and future AI-driven decisions.

    Attributes
    ----------
    recommendation:
        Primary recommendation produced by the system.
    reasons:
        Supporting reasons explaining why the recommendation was made.
    confidence:
        Confidence score for the recommendation in the range [0.0, 1.0].
    alternatives:
        Alternative recommendations considered by the system.
    tradeoffs:
        Advantages, disadvantages, or limitations associated with the
        recommendation.
    metadata:
        Additional contextual information associated with the explanation.
    """

    recommendation: str = Field(
        ...,
        description="Primary recommendation produced by the system.",
    )

    reasons: list[DecisionReason] = Field(
        default_factory=list,
        description="Supporting reasons for the recommendation.",
    )

    confidence: float = Field(
        default=1.0,
        ge=0.0,
        le=1.0,
        description="Confidence score for the recommendation.",
    )

    alternatives: list[str] = Field(
        default_factory=list,
        description="Alternative recommendations considered.",
    )

    tradeoffs: list[str] = Field(
        default_factory=list,
        description="Advantages, disadvantages, and limitations.",
    )

    metadata: dict[str, Any] = Field(
        default_factory=dict,
        description="Additional contextual information.",
    )
