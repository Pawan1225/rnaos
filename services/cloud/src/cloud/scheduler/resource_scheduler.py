"""
RNAOS Resource Scheduler.
"""

from __future__ import annotations

from cloud.scheduler.compute_resource import ComputeResource
from cloud.scheduler.highest_capacity_policy import (
    HighestCapacityPolicy,
)
from cloud.scheduler.resource_registry import (
    ResourceRegistry,
)
from cloud.scheduler.scheduling_policy import (
    SchedulingPolicy,
)


class ResourceScheduler:
    """Coordinates resource selection."""

    def __init__(
        self,
        registry: ResourceRegistry | None = None,
        policy: SchedulingPolicy | None = None,
    ) -> None:
        self._registry = registry if registry is not None else ResourceRegistry()

        self._policy = policy if policy is not None else HighestCapacityPolicy()

    @property
    def registry(
        self,
    ) -> ResourceRegistry:
        """Return the resource registry."""
        return self._registry

    def register(
        self,
        resource: ComputeResource,
    ) -> None:
        """Register a compute resource."""
        self._registry.register(resource)

    def unregister(
        self,
        identifier: str,
    ) -> None:
        """Unregister a compute resource."""
        self._registry.unregister(identifier)

    def resources(
        self,
    ) -> list[ComputeResource]:
        """Return all registered resources."""
        return self._registry.list_resources()

    def resource_count(
        self,
    ) -> int:
        """Return the number of registered resources."""
        return self._registry.resource_count()

    def schedule(
        self,
        kind: str,
    ) -> ComputeResource | None:
        """Select the best available resource."""

        candidates = self._registry.available(
            kind,
        )

        return self._policy.select(
            candidates,
        )
