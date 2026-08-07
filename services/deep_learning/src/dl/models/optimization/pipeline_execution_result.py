"""
RNAOS pipeline execution result model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class PipelineExecutionResult:
    """
    Immutable pipeline execution result.
    """

    pipeline_id: int

    completed_stages: int

    status: str
