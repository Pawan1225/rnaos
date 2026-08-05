from enterprise.deployment import (
    DeploymentEnvironment,
    DeploymentProfile,
    DeploymentStatus,
)


def test_profile_defaults():

    profile = DeploymentProfile(
        name="development",
        environment=DeploymentEnvironment.DEVELOPMENT,
        version="1.0.0",
    )

    assert profile.status == DeploymentStatus.PENDING

    assert profile.metadata == {}


def test_environment():

    assert DeploymentEnvironment.PRODUCTION == "production"


def test_status():

    assert DeploymentStatus.RUNNING == "running"
