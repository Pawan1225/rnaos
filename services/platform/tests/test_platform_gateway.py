from rnaos_platform.gateway import (
    GatewayContext,
    GatewayRequest,
    PlatformGateway,
)
from rnaos_platform.monitoring import (
    ComponentHealth,
    HealthCheck,
    HealthStatus,
)
from rnaos_platform.registry import (
    ServiceInfo,
)


class HealthyService(HealthCheck):
    """Dummy health check."""

    @property
    def name(self) -> str:
        return "gateway"

    def check(self) -> ComponentHealth:
        return ComponentHealth(
            name="gateway",
            status=HealthStatus.HEALTHY,
        )


def test_gateway_context() -> None:
    gateway = PlatformGateway()

    assert gateway.context is not None


def test_service_registration() -> None:
    gateway = PlatformGateway()

    gateway.context.registry.register(
        ServiceInfo(
            name="analytics",
            version="1.0.0",
            description="Analytics",
        ),
    )

    assert gateway.services() == [
        "analytics",
    ]


def test_unknown_service() -> None:
    gateway = PlatformGateway()

    response = gateway.execute(
        GatewayRequest(
            service="unknown",
            operation="run",
        ),
    )

    assert not response.success
    assert response.errors


def test_known_service() -> None:
    gateway = PlatformGateway()

    gateway.context.registry.register(
        ServiceInfo(
            name="solver",
            version="1.0.0",
            description="Solver",
        ),
    )

    response = gateway.execute(
        GatewayRequest(
            service="solver",
            operation="optimize",
            payload={
                "sequence": "AUGC",
            },
        ),
    )

    assert response.success
    assert response.data["service"] == "solver"


def test_configuration() -> None:
    gateway = PlatformGateway()

    gateway.configuration().set(
        "platform.mode",
        "test",
    )

    assert (
        gateway.configuration().get(
            "platform.mode",
        )
        == "test"
    )


def test_health_report() -> None:
    context = GatewayContext()

    context.health.register(
        HealthyService(),
    )

    gateway = PlatformGateway(
        context=context,
    )

    report = gateway.health()

    assert report.healthy


def test_observability_logging() -> None:
    gateway = PlatformGateway()

    gateway.context.registry.register(
        ServiceInfo(
            name="solver",
            version="1.0.0",
            description="Solver",
        ),
    )

    gateway.execute(
        GatewayRequest(
            service="solver",
            operation="run",
        ),
    )

    assert (
        len(
            gateway.context.observability.logs(),
        )
        == 1
    )


def test_workflow_access() -> None:
    gateway = PlatformGateway()

    assert gateway.workflow() is not None
