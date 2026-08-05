from enterprise.deployment import (
    DeploymentEnvironment,
    DeploymentManager,
    DeploymentProfile,
)


def test_register_profile():

    manager = DeploymentManager()

    manager.register(
        DeploymentProfile(
            name="development",
            environment=DeploymentEnvironment.DEVELOPMENT,
            version="1.0.0",
        )
    )

    assert manager.count() == 1


def test_get_profile():

    manager = DeploymentManager()

    profile = DeploymentProfile(
        name="production",
        environment=DeploymentEnvironment.PRODUCTION,
        version="1.0.0",
    )

    manager.register(profile)

    assert manager.get("production") is profile


def test_exists():

    manager = DeploymentManager()

    manager.register(
        DeploymentProfile(
            name="staging",
            environment=DeploymentEnvironment.STAGING,
            version="1.0.0",
        )
    )

    assert manager.exists("staging")


def test_remove():

    manager = DeploymentManager()

    manager.register(
        DeploymentProfile(
            name="testing",
            environment=DeploymentEnvironment.TESTING,
            version="1.0.0",
        )
    )

    manager.remove("testing")

    assert manager.count() == 0


def test_list_profiles():

    manager = DeploymentManager()

    manager.register(
        DeploymentProfile(
            name="production",
            environment=DeploymentEnvironment.PRODUCTION,
            version="1.0.0",
        )
    )

    manager.register(
        DeploymentProfile(
            name="development",
            environment=DeploymentEnvironment.DEVELOPMENT,
            version="1.0.0",
        )
    )

    profiles = manager.list_profiles()

    assert len(profiles) == 2

    assert profiles[0].name == "development"
