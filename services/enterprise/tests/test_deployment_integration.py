from enterprise.deployment import (
    DeploymentEnvironment,
    DeploymentManager,
    DeploymentProfile,
    DeploymentStatus,
    LocalDeploymentPolicy,
)


def test_deployment_workflow():

    manager = DeploymentManager()

    profile = DeploymentProfile(
        name="production",
        environment=DeploymentEnvironment.PRODUCTION,
        version="1.0.0",
    )

    manager.register(profile)

    assert manager.exists("production")

    deployment = manager.get("production")

    assert deployment is not None

    policy = LocalDeploymentPolicy()

    deployed = policy.deploy(deployment)

    assert deployed.status == DeploymentStatus.RUNNING

    assert manager.count() == 1
