"""
Compute resource model.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from cloud.scheduler.resource_kind import ResourceKind


@dataclass(slots=True)
class ComputeResource:
    """Represents one compute resource."""

    resource_id: str

    kind: ResourceKind

    hostname: str

    capacity: int

    available: bool = True

    active_jobs: int = 0

    metadata: dict[str, Any] = field(
        default_factory=dict,
    )

    def can_schedule(self) -> bool:
        """Return True if the resource is available."""
        return self.available

    @property
    def utilization(self) -> float:
        """Return utilization ratio."""
        if self.capacity <= 0:
            return 1.0

        return self.active_jobs / self.capacity

    def assign_job(self) -> None:
        """Assign one job to this resource."""
        self.active_jobs += 1

    def complete_job(self) -> None:
        """Complete one job."""
        if self.active_jobs > 0:
            self.active_jobs -= 1
