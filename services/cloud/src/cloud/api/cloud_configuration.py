"""
RNAOS Cloud configuration.
"""

from __future__ import annotations

from dataclasses import dataclass

from cloud.artifacts import ArtifactStore
from cloud.cache import DistributedCache
from cloud.cluster import ClusterManager
from cloud.execution import DistributedExecutionManager
from cloud.queue import JobQueue
from cloud.scheduler import ResourceScheduler


@dataclass(slots=True)
class CloudConfiguration:
    """Dependency injection container for CloudAPI."""

    execution: DistributedExecutionManager

    scheduler: ResourceScheduler

    queue: JobQueue

    artifacts: ArtifactStore

    cache: DistributedCache

    cluster: ClusterManager
