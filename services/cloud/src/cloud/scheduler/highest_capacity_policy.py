"""
Highest-capacity scheduling policy.
"""

from __future__ import annotations

from cloud.scheduler.compute_resource import ComputeResource
from cloud.scheduler.scheduling_policy import SchedulingPolicy


class HighestCapacityPolicy(SchedulingPolicy):
    """Select the available resource with the highest capacity."""

    def select(
        self,
        resources: list[ComputeResource],
    ) -> ComputeResource | None:
        """Return the resource with the highest capacity."""

        if not resources:
            return None

        return max(
            resources,
            key=lambda resource: resource.capacity,
        )
