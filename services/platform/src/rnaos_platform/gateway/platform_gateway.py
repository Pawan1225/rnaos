"""
RNAOS Platform Gateway.
"""

from __future__ import annotations

from datetime import UTC, datetime

from rnaos_platform.gateway.gateway_context import (
    GatewayContext,
)
from rnaos_platform.gateway.gateway_request import (
    GatewayRequest,
)
from rnaos_platform.gateway.gateway_response import (
    GatewayResponse,
)
from rnaos_platform.observability import (
    LogLevel,
    TraceRecord,
)


class PlatformGateway:
    """Unified entry point for the RNAOS platform."""

    def __init__(
        self,
        context: GatewayContext | None = None,
    ) -> None:
        self._context = context if context is not None else GatewayContext()

    @property
    def context(
        self,
    ) -> GatewayContext:
        """Return the gateway context."""
        return self._context

    def execute(
        self,
        request: GatewayRequest,
    ) -> GatewayResponse:
        """Execute a gateway request."""

        started = datetime.now(
            UTC,
        )

        self._context.observability.log(
            level=LogLevel.INFO,
            component="gateway",
            message=(f"{request.service}.{request.operation}"),
            trace_id=request.trace_id,
            metadata={
                "request_id": request.request_id,
            },
        )

        self._context.observability.trace(
            TraceRecord(
                trace_id=request.trace_id,
                component="gateway",
                operation=request.operation,
            ),
        )

        service = self._context.registry.get(
            request.service,
        )

        if service is None:
            finished = datetime.now(
                UTC,
            )

            return GatewayResponse(
                success=False,
                errors=[
                    (f"Unknown service: {request.service}"),
                ],
                trace_id=request.trace_id,
                request_id=request.request_id,
                duration_ms=(finished - started).total_seconds() * 1000,
            )

        finished = datetime.now(
            UTC,
        )

        return GatewayResponse(
            success=True,
            data={
                "service": service.name,
                "operation": request.operation,
                "payload": request.payload,
            },
            trace_id=request.trace_id,
            request_id=request.request_id,
            duration_ms=(finished - started).total_seconds() * 1000,
        )

    def services(
        self,
    ) -> list[str]:
        """Return registered service names."""
        return [service.name for service in self._context.registry.list_services()]

    def health(
        self,
    ):
        """Return the platform health report."""
        return self._context.health.report()

    def workflow(
        self,
    ):
        """Return the workflow engine."""
        return self._context.workflow

    def configuration(
        self,
    ):
        """Return the configuration manager."""
        return self._context.config
