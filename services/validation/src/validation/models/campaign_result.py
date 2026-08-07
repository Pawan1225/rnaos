"""
RNAOS benchmark campaign result model.
"""

from __future__ import annotations

from dataclasses import dataclass

from validation.models.experiment_result import (
    ExperimentResult,
)


@dataclass(
    slots=True,
    frozen=True,
)
class CampaignResult:
    """
    Immutable campaign execution result.
    """

    campaign_id: str

    total_experiments: int

    completed_experiments: int

    failed_experiments: int

    benchmark_version: str

    experiment_results: tuple[ExperimentResult, ...]
