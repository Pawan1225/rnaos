"""
In-memory cluster backend.
"""

from __future__ import annotations

from threading import RLock

from cloud.cluster.cluster_backend import ClusterBackend
from cloud.cluster.cluster_node import ClusterNode
from cloud.cluster.node_state import NodeState


class MemoryClusterBackend(ClusterBackend):
    """Thread-safe in-memory cluster backend."""

    def __init__(self) -> None:
        self._nodes: dict[str, ClusterNode] = {}
        self._lock = RLock()

    def register(
        self,
        node: ClusterNode,
    ) -> None:
        with self._lock:
            self._nodes[node.identifier] = node

    def unregister(
        self,
        identifier: str,
    ) -> None:
        with self._lock:
            self._nodes.pop(identifier, None)

    def get(
        self,
        identifier: str,
    ) -> ClusterNode | None:
        with self._lock:
            return self._nodes.get(identifier)

    def nodes(
        self,
    ) -> list[ClusterNode]:
        with self._lock:
            return sorted(
                self._nodes.values(),
                key=lambda node: node.identifier,
            )

    def filter_by_state(
        self,
        state: NodeState,
    ) -> list[ClusterNode]:
        with self._lock:
            return [node for node in self._nodes.values() if node.state is state]

    def count(
        self,
    ) -> int:
        with self._lock:
            return len(self._nodes)

    def clear(
        self,
    ) -> None:
        with self._lock:
            self._nodes.clear()
