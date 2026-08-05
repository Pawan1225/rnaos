"""
RNAOS Cloud Builder.
"""

from __future__ import annotations

from cloud.api.cloud_api import CloudAPI
from cloud.api.cloud_configuration import (
    CloudConfiguration,
)
from cloud.artifacts import ArtifactStore
from cloud.cache import DistributedCache
from cloud.cluster import ClusterManager
from cloud.execution import (
    DistributedExecutionManager,
)
from cloud.queue import JobQueue
from cloud.scheduler import ResourceScheduler


class CloudBuilder:
    """Build a fully configured CloudAPI instance."""

    def __init__(self) -> None:
        self._configuration = CloudConfiguration(
            execution=DistributedExecutionManager(),
            scheduler=ResourceScheduler(),
            queue=JobQueue(),
            artifacts=ArtifactStore(),
            cache=DistributedCache(),
            cluster=ClusterManager(),
        )

    def with_execution(
        self,
        execution: DistributedExecutionManager,
    ) -> CloudBuilder:
        self._configuration.execution = execution
        return self

    def with_scheduler(
        self,
        scheduler: ResourceScheduler,
    ) -> CloudBuilder:
        self._configuration.scheduler = scheduler
        return self

    def with_queue(
        self,
        queue: JobQueue,
    ) -> CloudBuilder:
        self._configuration.queue = queue
        return self

    def with_artifacts(
        self,
        artifacts: ArtifactStore,
    ) -> CloudBuilder:
        self._configuration.artifacts = artifacts
        return self

    def with_cache(
        self,
        cache: DistributedCache,
    ) -> CloudBuilder:
        self._configuration.cache = cache
        return self

    def with_cluster(
        self,
        cluster: ClusterManager,
    ) -> CloudBuilder:
        self._configuration.cluster = cluster
        return self

    def build(
        self,
    ) -> CloudAPI:
        """Build the CloudAPI."""

        return CloudAPI(self._configuration)
