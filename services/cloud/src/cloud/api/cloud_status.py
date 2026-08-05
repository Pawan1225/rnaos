"""
RNAOS Cloud runtime status.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class CloudStatus:
    """Runtime snapshot of the cloud platform."""

    workers: int = 0

    resources: int = 0

    pending_jobs: int = 0

    artifacts: int = 0

    cache_entries: int = 0

    cluster_nodes: int = 0

    @property
    def idle(self) -> bool:
        """Return True if no jobs are pending."""

        return self.pending_jobs == 0

    @property
    def infrastructure_ready(self) -> bool:
        """Return True if the platform has execution infrastructure."""

        return self.workers > 0 and self.resources > 0 and self.cluster_nodes > 0
