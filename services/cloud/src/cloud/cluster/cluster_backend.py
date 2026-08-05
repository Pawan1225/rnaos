"""
RNAOS cluster backend interface.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from cloud.cluster.cluster_node import ClusterNode
from cloud.cluster.node_state import NodeState


class ClusterBackend(ABC):
    """Abstract cluster backend."""

    @abstractmethod
    def register(
        self,
        node: ClusterNode,
    ) -> None:
        """Register a cluster node."""
        raise NotImplementedError

    @abstractmethod
    def unregister(
        self,
        identifier: str,
    ) -> None:
        """Remove a cluster node."""
        raise NotImplementedError

    @abstractmethod
    def get(
        self,
        identifier: str,
    ) -> ClusterNode | None:
        """Return a node by identifier."""
        raise NotImplementedError

    @abstractmethod
    def nodes(
        self,
    ) -> list[ClusterNode]:
        """Return all cluster nodes."""
        raise NotImplementedError

    @abstractmethod
    def filter_by_state(
        self,
        state: NodeState,
    ) -> list[ClusterNode]:
        """Return nodes matching a state."""
        raise NotImplementedError

    @abstractmethod
    def count(
        self,
    ) -> int:
        """Return the number of nodes."""
        raise NotImplementedError

    @abstractmethod
    def clear(
        self,
    ) -> None:
        """Remove all nodes."""
        raise NotImplementedError
