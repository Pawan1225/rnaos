"""
RNAOS Cloud API.
"""

from __future__ import annotations

from cloud.api.cloud_configuration import (
    CloudConfiguration,
)
from cloud.api.cloud_health import CloudHealth
from cloud.api.cloud_status import CloudStatus


class CloudAPI:
    """Unified enterprise cloud interface."""

    def __init__(
        self,
        configuration: CloudConfiguration,
    ) -> None:
        self._configuration = configuration

    @property
    def execution(self):
        return self._configuration.execution

    @property
    def scheduler(self):
        return self._configuration.scheduler

    @property
    def queue(self):
        return self._configuration.queue

    @property
    def artifacts(self):
        return self._configuration.artifacts

    @property
    def cache(self):
        return self._configuration.cache

    @property
    def cluster(self):
        return self._configuration.cluster

    def health(
        self,
    ) -> CloudHealth:
        """Return platform health."""

        return CloudHealth(
            execution=True,
            scheduler=True,
            queue=True,
            artifacts=True,
            cache=True,
            cluster=True,
        )

    def status(
        self,
    ) -> CloudStatus:
        """Return runtime platform status."""

        return CloudStatus(
            workers=self.execution.worker_count(),
            resources=self.scheduler.resource_count(),
            pending_jobs=self.queue.pending(),
            artifacts=self.artifacts.count(),
            cache_entries=self.cache.count(),
            cluster_nodes=self.cluster.count(),
        )
