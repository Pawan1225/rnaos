"""
RNAOS gateway context.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from rnaos_platform.config import ConfigManager
from rnaos_platform.events import EventBus
from rnaos_platform.monitoring import HealthMonitor
from rnaos_platform.observability import Observability
from rnaos_platform.registry import ServiceRegistry
from rnaos_platform.workflow import WorkflowEngine


@dataclass(
    slots=True,
)
class GatewayContext:
    """Shared platform services used by the API gateway."""

    config: ConfigManager = field(
        default_factory=ConfigManager,
    )

    registry: ServiceRegistry = field(
        default_factory=ServiceRegistry,
    )

    event_bus: EventBus = field(
        default_factory=EventBus,
    )

    workflow: WorkflowEngine = field(
        default_factory=WorkflowEngine,
    )

    health: HealthMonitor = field(
        default_factory=HealthMonitor,
    )

    observability: Observability = field(
        default_factory=Observability,
    )
