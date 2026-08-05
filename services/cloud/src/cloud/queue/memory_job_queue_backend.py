"""
In-memory job queue backend.
"""

from __future__ import annotations

from collections import deque
from dataclasses import replace

from cloud.queue.job import Job
from cloud.queue.job_queue_backend import JobQueueBackend
from cloud.queue.job_status import JobStatus


class MemoryJobQueueBackend(JobQueueBackend):
    """In-memory FIFO job queue backend."""

    def __init__(self) -> None:
        self._queue: deque[Job] = deque()

    def submit(
        self,
        job: Job,
    ) -> None:
        queued_job = replace(
            job,
            status=JobStatus.QUEUED,
        )

        self._queue.append(queued_job)

    def next_job(
        self,
    ) -> Job | None:
        if not self._queue:
            return None

        job = self._queue.popleft()

        return replace(
            job,
            status=JobStatus.RUNNING,
        )

    def complete(
        self,
        job: Job,
    ) -> None:
        # Immutable Job objects are not modified.
        # Completion state is returned to the caller.
        return

    def pending(
        self,
    ) -> int:
        return len(self._queue)
