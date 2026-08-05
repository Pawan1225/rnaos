"""
Job queue backend abstraction.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from cloud.queue.job import Job


class JobQueueBackend(ABC):
    """Abstract job queue backend."""

    @abstractmethod
    def submit(
        self,
        job: Job,
    ) -> None:
        """Submit a job to the queue."""
        raise NotImplementedError

    @abstractmethod
    def next_job(
        self,
    ) -> Job | None:
        """Return the next available job."""
        raise NotImplementedError

    @abstractmethod
    def complete(
        self,
        job: Job,
    ) -> None:
        """Mark a job as completed."""
        raise NotImplementedError

    @abstractmethod
    def pending(
        self,
    ) -> int:
        """Return the number of pending jobs."""
        raise NotImplementedError
