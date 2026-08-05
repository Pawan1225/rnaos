from enterprise.deployment import (
    DeploymentEnvironment,
    DeploymentProfile,
    DeploymentRegistry,
)


def test_register_profile():

    registry = DeploymentRegistry()

    registry.register(
        DeploymentProfile(
            name="development",
            environment=DeploymentEnvironment.DEVELOPMENT,
            version="1.0.0",
        )
    )

    assert registry.count() == 1


def test_lookup_profile():

    registry = DeploymentRegistry()

    profile = DeploymentProfile(
        name="production",
        environment=DeploymentEnvironment.PRODUCTION,
        version="1.0.0",
    )

    registry.register(profile)

    assert registry.get("production") is profile


def test_remove_profile():

    registry = DeploymentRegistry()

    registry.register(
        DeploymentProfile(
            name="staging",
            environment=DeploymentEnvironment.STAGING,
            version="1.0.0",
        )
    )

    registry.remove("staging")

    assert registry.count() == 0


def test_exists():

    registry = DeploymentRegistry()

    registry.register(
        DeploymentProfile(
            name="testing",
            environment=DeploymentEnvironment.TESTING,
            version="1.0.0",
        )
    )

    assert registry.exists("testing")

    assert not registry.exists("production")


def test_clear():

    registry = DeploymentRegistry()

    registry.register(
        DeploymentProfile(
            name="development",
            environment=DeploymentEnvironment.DEVELOPMENT,
            version="1.0.0",
        )
    )

    registry.register(
        DeploymentProfile(
            name="production",
            environment=DeploymentEnvironment.PRODUCTION,
            version="1.0.0",
        )
    )

    registry.clear()

    assert registry.count() == 0
