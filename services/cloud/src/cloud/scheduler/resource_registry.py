"""
Compute resource registry.
"""

from __future__ import annotations

from threading import RLock

from cloud.scheduler.compute_resource import ComputeResource
from cloud.scheduler.resource_kind import ResourceKind


class ResourceRegistry:
    """Thread-safe registry of compute resources."""

    def __init__(self) -> None:
        self._resources: dict[str, ComputeResource] = {}
        self._lock = RLock()

    def register(
        self,
        resource: ComputeResource,
    ) -> None:
        """Register a compute resource."""
        with self._lock:
            self._resources[resource.resource_id] = resource

    def unregister(
        self,
        resource_id: str,
    ) -> None:
        """Remove a compute resource."""
        with self._lock:
            self._resources.pop(resource_id, None)

    def get(
        self,
        resource_id: str,
    ) -> ComputeResource | None:
        """Return a resource by ID."""
        with self._lock:
            return self._resources.get(resource_id)

    def exists(
        self,
        resource_id: str,
    ) -> bool:
        """Return True if the resource exists."""
        with self._lock:
            return resource_id in self._resources

    def list_resources(self) -> list[ComputeResource]:
        """Return all resources sorted by ID."""
        with self._lock:
            return sorted(
                self._resources.values(),
                key=lambda resource: resource.resource_id,
            )

    def resource_count(self) -> int:
        """Return the number of registered resources."""
        with self._lock:
            return len(self._resources)

    def by_kind(
        self,
        kind: ResourceKind,
    ) -> list[ComputeResource]:
        """Return resources of a given kind."""
        with self._lock:
            return [resource for resource in self._resources.values() if resource.kind == kind]

    def available(
        self,
        kind: ResourceKind | None = None,
    ) -> list[ComputeResource]:
        """
        Return available resources.

        If a resource kind is provided, only resources of that kind
        are returned.
        """
        with self._lock:
            resources = [
                resource for resource in self._resources.values() if resource.can_schedule()
            ]

            if kind is not None:
                resources = [resource for resource in resources if resource.kind == kind]

            return sorted(
                resources,
                key=lambda resource: resource.resource_id,
            )
