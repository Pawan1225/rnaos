from enterprise.security import (
    AuthorizationManager,
    User,
    UserRegistry,
)


def test_has_role():

    registry = UserRegistry()

    registry.register(
        User(
            username="alice",
            role="admin",
        )
    )

    authz = AuthorizationManager(registry)

    assert authz.has_role(
        "alice",
        "admin",
    )


def test_wrong_role():

    registry = UserRegistry()

    registry.register(
        User(
            username="alice",
            role="admin",
        )
    )

    authz = AuthorizationManager(registry)

    assert not authz.has_role(
        "alice",
        "researcher",
    )


def test_permission():

    registry = UserRegistry()

    registry.register(
        User(
            username="alice",
            role="admin",
            metadata={
                "permissions": {
                    "deploy",
                    "manage_users",
                },
            },
        )
    )

    authz = AuthorizationManager(registry)

    assert authz.has_permission(
        "alice",
        "deploy",
    )


def test_missing_permission():

    registry = UserRegistry()

    registry.register(
        User(
            username="alice",
            role="admin",
            metadata={
                "permissions": {
                    "deploy",
                },
            },
        )
    )

    authz = AuthorizationManager(registry)

    assert not authz.has_permission(
        "alice",
        "delete_cluster",
    )


def test_authorize():

    registry = UserRegistry()

    registry.register(
        User(
            username="alice",
            role="admin",
            metadata={
                "permissions": {
                    "deploy",
                },
            },
        )
    )

    authz = AuthorizationManager(registry)

    assert authz.authorize(
        "alice",
        role="admin",
        permission="deploy",
    )
