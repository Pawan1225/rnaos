"""
RNAOS Distributed Execution Manager.
"""

from __future__ import annotations

from cloud.execution.dispatcher import Dispatcher
from cloud.execution.execution_request import ExecutionRequest
from cloud.execution.execution_result import ExecutionResult
from cloud.execution.execution_status import ExecutionStatus
from cloud.execution.worker import Worker
from cloud.execution.worker_registry import WorkerRegistry


class DistributedExecutionManager:
    """Coordinate distributed execution across registered workers."""

    def __init__(
        self,
        registry: WorkerRegistry | None = None,
    ) -> None:
        self._registry = registry if registry is not None else WorkerRegistry()

        self._dispatcher = Dispatcher(
            self._registry,
        )

    @property
    def registry(
        self,
    ) -> WorkerRegistry:
        """Return the worker registry."""
        return self._registry

    def register_worker(
        self,
        worker: Worker,
    ) -> None:
        """Register a worker."""
        self._registry.register(worker)

    def unregister_worker(
        self,
        worker_id: str,
    ) -> None:
        """Remove a worker."""
        self._registry.unregister(worker_id)

    def workers(
        self,
    ) -> list[Worker]:
        """Return all registered workers."""
        return self._registry.list_workers()

    def worker_count(
        self,
    ) -> int:
        """Return the number of registered workers."""
        return self._registry.worker_count()

    def execute(
        self,
        request: ExecutionRequest,
    ) -> ExecutionResult:
        """Dispatch an execution request."""

        worker = self._dispatcher.select_worker()

        if worker is None:
            return ExecutionResult(
                status=ExecutionStatus.FAILED,
                worker_id=None,
                result=None,
                message="No available workers.",
            )

        worker.active_jobs += 1

        try:
            return ExecutionResult(
                status=ExecutionStatus.COMPLETED,
                worker_id=worker.worker_id,
                result=request.payload,
                message="Execution completed.",
            )
        finally:
            worker.active_jobs -= 1
