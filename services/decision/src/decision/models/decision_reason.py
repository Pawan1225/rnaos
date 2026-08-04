from __future__ import annotations

from pydantic import BaseModel, Field

from decision.models.evidence import Evidence


class DecisionReason(BaseModel):
    """
    Human-readable explanation for a recommendation.

    A DecisionReason combines one or more pieces of evidence into a
    coherent justification that explains why a decision was made.

    Examples include:
    - Large optimization problem
    - Dense QUBO graph
    - Low predicted runtime
    - High folding confidence

    Attributes
    ----------
    title:
        Short title describing the reason.
    description:
        Detailed explanation of the reasoning.
    importance:
        Relative importance of this reason in the overall decision,
        constrained to the range [0.0, 1.0].
    evidence:
        Supporting evidence objects used to justify the reason.
    """

    title: str = Field(
        ...,
        description="Short title describing the decision reason.",
    )

    description: str = Field(
        ...,
        description="Detailed explanation of the reasoning.",
    )

    importance: float = Field(
        default=1.0,
        ge=0.0,
        le=1.0,
        description="Relative importance of this reason.",
    )

    evidence: list[Evidence] = Field(
        default_factory=list,
        description="Supporting evidence for this reason.",
    )
