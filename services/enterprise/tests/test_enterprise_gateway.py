from enterprise.gateway import EnterpriseGateway


def test_gateway_components():
    gateway = EnterpriseGateway()

    assert gateway.security is not None
    assert gateway.deployment is not None
    assert gateway.backup is not None
    assert gateway.validation is not None
    assert gateway.benchmark is not None
    assert gateway.release is not None


def test_services():
    gateway = EnterpriseGateway()

    services = gateway.services

    assert len(services) == 6

    assert "security" in services
    assert "deployment" in services
    assert "backup" in services
    assert "validation" in services
    assert "benchmark" in services
    assert "release" in services


def test_get_service():
    gateway = EnterpriseGateway()

    service = gateway.get_service(
        "validation",
    )

    assert service is gateway.validation


def test_has_service():
    gateway = EnterpriseGateway()

    assert gateway.has_service("security")

    assert not gateway.has_service(
        "quantum",
    )


def test_list_services():
    gateway = EnterpriseGateway()

    assert gateway.list_services() == [
        "backup",
        "benchmark",
        "deployment",
        "release",
        "security",
        "validation",
    ]


def test_health():
    gateway = EnterpriseGateway()

    health = gateway.health()

    assert len(health) == 6

    assert all(status == "healthy" for status in health.values())


def test_is_healthy():
    gateway = EnterpriseGateway()

    assert gateway.is_healthy()


def test_metadata():
    gateway = EnterpriseGateway()

    metadata = gateway.metadata()

    assert metadata["name"] == "RNAOS Enterprise Gateway"
    assert metadata["version"] == "1.0.0"
    assert metadata["build"] == "Sprint-13.7"


def test_summary():
    gateway = EnterpriseGateway()

    summary = gateway.summary()

    assert summary["service_count"] == 6
    assert len(summary["services"]) == 6
    assert summary["metadata"]["version"] == "1.0.0"
