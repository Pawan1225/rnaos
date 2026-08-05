"""
Supported artifact kinds.
"""

from __future__ import annotations

from enum import StrEnum


class ArtifactKind(StrEnum):
    """Supported artifact types."""

    REPORT = "report"

    MODEL = "model"

    DATASET = "dataset"

    PLOT = "plot"

    LOG = "log"

    BENCHMARK = "benchmark"

    CHECKPOINT = "checkpoint"

    OTHER = "other"
