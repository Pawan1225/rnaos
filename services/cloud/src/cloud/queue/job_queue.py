"""
RNAOS Job Queue.
"""

from __future__ import annotations

from cloud.queue.job import Job
from cloud.queue.job_queue_backend import JobQueueBackend
from cloud.queue.memory_job_queue_backend import (
    MemoryJobQueueBackend,
)


class JobQueue:
    """Public interface for RNAOS job queues."""

    def __init__(
        self,
        backend: JobQueueBackend | None = None,
    ) -> None:
        self._backend = backend if backend is not None else MemoryJobQueueBackend()

    def submit(
        self,
        job: Job,
    ) -> None:
        """Submit a job."""
        self._backend.submit(job)

    def next_job(
        self,
    ) -> Job | None:
        """Return the next available job."""
        return self._backend.next_job()

    def complete(
        self,
        job: Job,
    ) -> None:
        """Mark a job as completed."""
        self._backend.complete(job)

    def pending(
        self,
    ) -> int:
        """Return the number of pending jobs."""
        return self._backend.pending()
