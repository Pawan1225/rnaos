from enterprise.gateway import EnterpriseGateway
from enterprise.security import User


def test_enterprise_gateway_integration():
    gateway = EnterpriseGateway()

    gateway.security.register(
        User(
            username="admin",
            role="admin",
        )
    )

    assert gateway.security.count() == 1

    assert gateway.has_service("security")
    assert gateway.has_service("validation")
    assert gateway.has_service("benchmark")
    assert gateway.has_service("release")

    assert gateway.is_healthy()

    summary = gateway.summary()

    assert summary["service_count"] == 6
    assert summary["metadata"]["name"] == "RNAOS Enterprise Gateway"
    assert summary["metadata"]["version"] == "1.0.0"
