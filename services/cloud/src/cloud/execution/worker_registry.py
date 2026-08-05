"""
Worker registry for distributed execution.
"""

from __future__ import annotations

from threading import RLock

from cloud.execution.worker import Worker
from cloud.execution.worker_state import WorkerState


class WorkerRegistry:
    """Thread-safe registry of execution workers."""

    def __init__(self) -> None:
        self._workers: dict[str, Worker] = {}
        self._lock = RLock()

    def register(self, worker: Worker) -> None:
        """Register a worker."""
        with self._lock:
            self._workers[worker.worker_id] = worker

    def unregister(self, worker_id: str) -> None:
        """Remove a worker."""
        with self._lock:
            self._workers.pop(worker_id, None)

    def get(self, worker_id: str) -> Worker | None:
        """Return a worker by ID."""
        with self._lock:
            return self._workers.get(worker_id)

    def exists(self, worker_id: str) -> bool:
        """Return True if the worker exists."""
        with self._lock:
            return worker_id in self._workers

    def list_workers(self) -> list[Worker]:
        """Return all workers sorted by ID."""
        with self._lock:
            return sorted(
                self._workers.values(),
                key=lambda worker: worker.worker_id,
            )

    def worker_count(self) -> int:
        """Return the number of registered workers."""
        with self._lock:
            return len(self._workers)

    def by_state(
        self,
        state: WorkerState,
    ) -> list[Worker]:
        """Return workers in the given state."""
        with self._lock:
            return [worker for worker in self._workers.values() if worker.state == state]

    def by_capability(
        self,
        capability: str,
    ) -> list[Worker]:
        """Return workers supporting a capability."""
        with self._lock:
            return [
                worker for worker in self._workers.values() if capability in worker.capabilities
            ]

    def update_heartbeat(
        self,
        worker_id: str,
    ) -> None:
        """Update a worker heartbeat."""
        with self._lock:
            worker = self._workers.get(worker_id)

            if worker is not None:
                worker.heartbeat()
