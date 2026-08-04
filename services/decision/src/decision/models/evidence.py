from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class Evidence(BaseModel):
    """
    Structured evidence supporting a decision or recommendation.

    Each Evidence instance represents one measurable or observable fact
    used by the Decision Intelligence layer when explaining a result.
    Examples include problem size, QUBO density, estimated runtime,
    benchmark statistics, or folding energy.

    Attributes
    ----------
    name:
        Human-readable name of the evidence.
    value:
        Observed or computed value associated with the evidence.
    description:
        Explanation of what the evidence represents.
    source:
        Origin of the evidence (e.g., OptimizationProfiler,
        SolverBenchmark, FoldingEngine).
    weight:
        Relative importance of this evidence when constructing an
        explanation. Constrained to the range [0.0, 1.0].
    """

    name: str = Field(
        ...,
        description="Human-readable evidence name.",
    )

    value: Any = Field(
        ...,
        description="Observed or computed value.",
    )

    description: str = Field(
        ...,
        description="Description of the evidence.",
    )

    source: str = Field(
        ...,
        description="Component that produced the evidence.",
    )

    weight: float = Field(
        default=1.0,
        ge=0.0,
        le=1.0,
        description="Relative importance of this evidence.",
    )
