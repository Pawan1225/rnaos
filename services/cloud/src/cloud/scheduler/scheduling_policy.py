"""
Scheduling policy interface.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from cloud.scheduler.compute_resource import ComputeResource


class SchedulingPolicy(ABC):
    """Abstract base class for scheduling policies."""

    @abstractmethod
    def select(
        self,
        resources: list[ComputeResource],
    ) -> ComputeResource | None:
        """Select the best resource from the available candidates."""
        raise NotImplementedError
