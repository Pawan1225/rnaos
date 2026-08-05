"""
In-memory telemetry provider.
"""

from __future__ import annotations

from rnaos_platform.observability.log_record import (
    LogRecord,
)
from rnaos_platform.observability.metric_record import (
    MetricRecord,
)
from rnaos_platform.observability.telemetry_provider import (
    TelemetryProvider,
)
from rnaos_platform.observability.trace_record import (
    TraceRecord,
)


class MemoryTelemetryProvider(
    TelemetryProvider,
):
    """Store telemetry records in memory."""

    def __init__(
        self,
    ) -> None:
        self._logs: list[LogRecord] = []

        self._metrics: list[MetricRecord] = []

        self._traces: list[TraceRecord] = []

    def record_log(
        self,
        record: LogRecord,
    ) -> None:
        """Store a log record."""
        self._logs.append(
            record,
        )

    def record_metric(
        self,
        record: MetricRecord,
    ) -> None:
        """Store a metric record."""
        self._metrics.append(
            record,
        )

    def record_trace(
        self,
        record: TraceRecord,
    ) -> None:
        """Store a trace record."""
        self._traces.append(
            record,
        )

    def logs(
        self,
    ) -> tuple[
        LogRecord,
        ...,
    ]:
        """Return all log records."""
        return tuple(
            self._logs,
        )

    def metrics(
        self,
    ) -> tuple[
        MetricRecord,
        ...,
    ]:
        """Return all metric records."""
        return tuple(
            self._metrics,
        )

    def traces(
        self,
    ) -> tuple[
        TraceRecord,
        ...,
    ]:
        """Return all trace records."""
        return tuple(
            self._traces,
        )

    def clear(
        self,
    ) -> None:
        """Clear all telemetry."""
        self._logs.clear()

        self._metrics.clear()

        self._traces.clear()
