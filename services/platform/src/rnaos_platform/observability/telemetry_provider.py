"""
RNAOS telemetry provider abstraction.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from rnaos_platform.observability.log_record import (
    LogRecord,
)
from rnaos_platform.observability.metric_record import (
    MetricRecord,
)
from rnaos_platform.observability.trace_record import (
    TraceRecord,
)


class TelemetryProvider(ABC):
    """Base class for telemetry providers."""

    @abstractmethod
    def record_log(
        self,
        record: LogRecord,
    ) -> None:
        """Record a structured log."""

    @abstractmethod
    def record_metric(
        self,
        record: MetricRecord,
    ) -> None:
        """Record a metric."""

    @abstractmethod
    def record_trace(
        self,
        record: TraceRecord,
    ) -> None:
        """Record a trace."""

    @abstractmethod
    def logs(
        self,
    ) -> tuple[LogRecord, ...]:
        """Return recorded logs."""

    @abstractmethod
    def metrics(
        self,
    ) -> tuple[MetricRecord, ...]:
        """Return recorded metrics."""

    @abstractmethod
    def traces(
        self,
    ) -> tuple[TraceRecord, ...]:
        """Return recorded traces."""

    @abstractmethod
    def clear(
        self,
    ) -> None:
        """Clear all telemetry."""
