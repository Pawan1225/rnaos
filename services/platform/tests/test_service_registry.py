from rnaos_platform.registry import (
    ServiceInfo,
    ServiceRegistry,
)


def test_register_service() -> None:
    registry = ServiceRegistry()

    registry.register(
        ServiceInfo(
            name="solver",
            version="1.0.0",
            description="Solver Service",
        ),
    )

    assert registry.count() == 1
    assert registry.exists("solver")


def test_get_service() -> None:
    registry = ServiceRegistry()

    service = ServiceInfo(
        name="analytics",
        version="1.0.0",
        description="Analytics Service",
    )

    registry.register(service)

    assert registry.get("analytics") == service


def test_unregister_service() -> None:
    registry = ServiceRegistry()

    registry.register(
        ServiceInfo(
            name="decision",
            version="1.0.0",
            description="Decision Service",
        ),
    )

    registry.unregister("decision")

    assert not registry.exists("decision")


def test_list_services() -> None:
    registry = ServiceRegistry()

    registry.register(
        ServiceInfo(
            name="solver",
            version="1.0.0",
            description="Solver",
        ),
    )

    registry.register(
        ServiceInfo(
            name="analytics",
            version="1.0.0",
            description="Analytics",
        ),
    )

    services = registry.list_services()

    assert len(services) == 2
    assert services[0].name == "analytics"
    assert services[1].name == "solver"


def test_empty_registry() -> None:
    registry = ServiceRegistry()

    assert registry.count() == 0
    assert registry.list_services() == []
    assert registry.get("missing") is None
    assert not registry.exists("missing")
