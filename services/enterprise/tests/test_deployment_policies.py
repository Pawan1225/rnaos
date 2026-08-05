from enterprise.deployment import (
    DeploymentEnvironment,
    DeploymentProfile,
    DeploymentStatus,
    LocalDeploymentPolicy,
)


def test_local_policy():

    profile = DeploymentProfile(
        name="development",
        environment=DeploymentEnvironment.DEVELOPMENT,
        version="1.0.0",
    )

    policy = LocalDeploymentPolicy()

    deployed = policy.deploy(profile)

    assert deployed.status == DeploymentStatus.RUNNING
