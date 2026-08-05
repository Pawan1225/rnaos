from rnaos_platform.events import (
    Event,
    EventBus,
    EventType,
)
from rnaos_platform.monitoring import (
    ComponentHealth,
    HealthCheck,
    HealthMonitor,
    HealthStatus,
)


class DummyHealthCheck(HealthCheck):
    """Simple health check used for testing."""

    def __init__(
        self,
        name: str,
        status: HealthStatus,
    ) -> None:
        self._name = name
        self._status = status

    @property
    def name(
        self,
    ) -> str:
        return self._name

    def check(
        self,
    ) -> ComponentHealth:
        return ComponentHealth(
            name=self._name,
            status=self._status,
        )


def test_healthy_report() -> None:
    monitor = HealthMonitor()

    monitor.register(
        DummyHealthCheck(
            "solver",
            HealthStatus.HEALTHY,
        ),
    )

    report = monitor.report()

    assert report.healthy
    assert report.overall_status == HealthStatus.HEALTHY


def test_warning_report() -> None:
    monitor = HealthMonitor()

    monitor.register(
        DummyHealthCheck(
            "analytics",
            HealthStatus.WARNING,
        ),
    )

    report = monitor.report()

    assert report.overall_status == HealthStatus.WARNING


def test_critical_report() -> None:
    monitor = HealthMonitor()

    monitor.register(
        DummyHealthCheck(
            "workflow",
            HealthStatus.CRITICAL,
        ),
    )

    report = monitor.report()

    assert report.overall_status == HealthStatus.CRITICAL


def test_unknown_report() -> None:
    monitor = HealthMonitor()

    monitor.register(
        DummyHealthCheck(
            "registry",
            HealthStatus.UNKNOWN,
        ),
    )

    report = monitor.report()

    assert report.overall_status == HealthStatus.UNKNOWN


def test_register_unregister() -> None:
    monitor = HealthMonitor()

    monitor.register(
        DummyHealthCheck(
            "solver",
            HealthStatus.HEALTHY,
        ),
    )

    assert monitor.component_count() == 1

    monitor.unregister(
        "solver",
    )

    assert monitor.component_count() == 0


def test_clear() -> None:
    monitor = HealthMonitor()

    monitor.register(
        DummyHealthCheck(
            "solver",
            HealthStatus.HEALTHY,
        ),
    )

    monitor.clear()

    assert monitor.component_count() == 0


def test_health_changed_event() -> None:
    bus = EventBus()

    received: list[EventType] = []

    def handler(
        event: Event,
    ) -> None:
        received.append(
            event.event_type,
        )

    bus.subscribe(
        EventType.HEALTH_CHANGED,
        handler,
    )

    monitor = HealthMonitor(
        event_bus=bus,
    )

    monitor.register(
        DummyHealthCheck(
            "solver",
            HealthStatus.HEALTHY,
        ),
    )

    monitor.report()

    assert EventType.HEALTH_CHANGED in received


def test_report_is_immutable() -> None:
    monitor = HealthMonitor()

    monitor.register(
        DummyHealthCheck(
            "solver",
            HealthStatus.HEALTHY,
        ),
    )

    report = monitor.report()

    assert isinstance(
        report.components,
        tuple,
    )
