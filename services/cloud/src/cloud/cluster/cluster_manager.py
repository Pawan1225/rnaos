"""
RNAOS Cluster Manager.
"""

from __future__ import annotations

from cloud.cluster.cluster_backend import ClusterBackend
from cloud.cluster.cluster_node import ClusterNode
from cloud.cluster.cluster_statistics import ClusterStatistics
from cloud.cluster.memory_cluster_backend import (
    MemoryClusterBackend,
)
from cloud.cluster.node_state import NodeState


class ClusterManager:
    """Public interface for cluster management."""

    def __init__(
        self,
        backend: ClusterBackend | None = None,
    ) -> None:
        self._backend = backend if backend is not None else MemoryClusterBackend()

    def register(
        self,
        node: ClusterNode,
    ) -> None:
        self._backend.register(node)

    def unregister(
        self,
        identifier: str,
    ) -> None:
        self._backend.unregister(identifier)

    def get(
        self,
        identifier: str,
    ) -> ClusterNode | None:
        return self._backend.get(identifier)

    def nodes(
        self,
    ) -> list[ClusterNode]:
        return self._backend.nodes()

    def filter_by_state(
        self,
        state: NodeState,
    ) -> list[ClusterNode]:
        return self._backend.filter_by_state(state)

    def count(
        self,
    ) -> int:
        return self._backend.count()

    def clear(
        self,
    ) -> None:
        self._backend.clear()

    def statistics(
        self,
    ) -> ClusterStatistics:
        """Compute runtime cluster statistics."""

        nodes = self._backend.nodes()

        stats = ClusterStatistics()

        stats.total_nodes = len(nodes)

        stats.online_nodes = sum(node.state is NodeState.ONLINE for node in nodes)

        stats.offline_nodes = sum(node.state is NodeState.OFFLINE for node in nodes)

        stats.failed_nodes = sum(node.state is NodeState.FAILED for node in nodes)

        stats.total_cpu_cores = sum(node.cpu_cores for node in nodes)

        stats.total_gpu_count = sum(node.gpu_count for node in nodes)

        stats.total_memory_gb = sum(node.memory_gb for node in nodes)

        return stats
