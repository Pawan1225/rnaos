"""
RNAOS cluster node.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime

from cloud.cluster.node_state import NodeState


@dataclass(slots=True)
class ClusterNode:
    """Represents a node in an RNAOS cluster."""

    identifier: str

    hostname: str

    state: NodeState = NodeState.ONLINE

    cpu_cores: int = 0

    gpu_count: int = 0

    memory_gb: float = 0.0

    accelerators: set[str] = field(
        default_factory=set,
    )

    capabilities: set[str] = field(
        default_factory=set,
    )

    labels: dict[str, str] = field(
        default_factory=dict,
    )

    metadata: dict[str, object] = field(
        default_factory=dict,
    )

    active_jobs: int = 0

    max_jobs: int = 1

    last_heartbeat: datetime = field(
        default_factory=lambda: datetime.now(UTC),
    )

    @property
    def available(self) -> bool:
        """Return True if the node can accept work."""
        return self.state is NodeState.ONLINE and self.active_jobs < self.max_jobs

    def heartbeat(self) -> None:
        """Update the heartbeat timestamp."""
        self.last_heartbeat = datetime.now(UTC)
