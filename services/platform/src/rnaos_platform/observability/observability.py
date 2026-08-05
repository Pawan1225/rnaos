"""
RNAOS observability facade.
"""

from __future__ import annotations

from typing import Any

from rnaos_platform.observability.log_level import (
    LogLevel,
)
from rnaos_platform.observability.log_record import (
    LogRecord,
)
from rnaos_platform.observability.metric_record import (
    MetricRecord,
)
from rnaos_platform.observability.providers.memory_provider import (
    MemoryTelemetryProvider,
)
from rnaos_platform.observability.telemetry_provider import (
    TelemetryProvider,
)
from rnaos_platform.observability.trace_record import (
    TraceRecord,
)


class Observability:
    """Unified observability interface."""

    def __init__(
        self,
        provider: TelemetryProvider | None = None,
    ) -> None:
        self._provider = provider if provider is not None else MemoryTelemetryProvider()

    def log(
        self,
        *,
        level: LogLevel,
        component: str,
        message: str,
        trace_id: str | None = None,
        workflow_id: str | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> None:
        """Record a structured log."""

        self._provider.record_log(
            LogRecord(
                level=level,
                component=component,
                message=message,
                trace_id=trace_id,
                workflow_id=workflow_id,
                metadata=metadata or {},
            ),
        )

    def metric(
        self,
        *,
        name: str,
        value: float,
        unit: str = "",
        labels: dict[str, str] | None = None,
    ) -> None:
        """Record a metric."""

        self._provider.record_metric(
            MetricRecord(
                name=name,
                value=value,
                unit=unit,
                labels=labels or {},
            ),
        )

    def trace(
        self,
        record: TraceRecord,
    ) -> None:
        """Record a trace."""

        self._provider.record_trace(
            record,
        )

    def logs(
        self,
    ) -> tuple[
        LogRecord,
        ...,
    ]:
        """Return all logs."""
        return self._provider.logs()

    def metrics(
        self,
    ) -> tuple[
        MetricRecord,
        ...,
    ]:
        """Return all metrics."""
        return self._provider.metrics()

    def traces(
        self,
    ) -> tuple[
        TraceRecord,
        ...,
    ]:
        """Return all traces."""
        return self._provider.traces()

    def clear(
        self,
    ) -> None:
        """Clear all telemetry."""

        self._provider.clear()
