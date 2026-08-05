"""
Worker dispatcher.
"""

from __future__ import annotations

from cloud.execution.worker import Worker
from cloud.execution.worker_registry import WorkerRegistry


class Dispatcher:
    """Dispatch execution requests to workers."""

    def __init__(
        self,
        registry: WorkerRegistry,
    ) -> None:
        self._registry = registry

    def select_worker(self) -> Worker | None:
        """
        Select the least-loaded worker.

        Returns
        -------
        Worker | None
            Selected worker or None if no worker is available.
        """

        candidates = [worker for worker in self._registry.list_workers() if worker.can_accept_job()]

        if not candidates:
            return None

        return min(
            candidates,
            key=lambda worker: (
                worker.active_jobs,
                worker.worker_id,
            ),
        )
