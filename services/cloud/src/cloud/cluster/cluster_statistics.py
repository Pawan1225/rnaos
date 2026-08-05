"""
Cluster statistics.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class ClusterStatistics:
    """Runtime cluster statistics."""

    total_nodes: int = 0

    online_nodes: int = 0

    offline_nodes: int = 0

    failed_nodes: int = 0

    total_cpu_cores: int = 0

    total_gpu_count: int = 0

    total_memory_gb: float = 0.0

    @property
    def utilization(self) -> float:
        """Return cluster availability ratio."""
        if self.total_nodes == 0:
            return 0.0

        return self.online_nodes / self.total_nodes
