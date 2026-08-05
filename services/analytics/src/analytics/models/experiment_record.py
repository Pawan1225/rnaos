"""
Analytics experiment record.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime


@dataclass(slots=True)
class ExperimentRecord:
    """Represents one RNAOS experiment."""

    experiment_id: str
    sequence: str
    solver: str
    objective_value: float
    runtime_seconds: float
    confidence: float

    timestamp: datetime = field(default_factory=lambda: datetime.now(UTC))

    metadata: dict[str, object] = field(default_factory=dict)

    @property
    def sequence_length(self) -> int:
        return len(self.sequence)
