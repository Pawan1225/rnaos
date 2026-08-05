from enterprise.security import (
    User,
    UserRegistry,
)


def test_register_user():

    registry = UserRegistry()

    registry.register(
        User(
            username="alice",
            role="admin",
        )
    )

    assert registry.count() == 1


def test_lookup_user():

    registry = UserRegistry()

    user = User(
        username="bob",
        role="researcher",
    )

    registry.register(user)

    assert registry.get("bob") is user


def test_remove_user():

    registry = UserRegistry()

    registry.register(
        User(
            username="charlie",
            role="admin",
        )
    )

    registry.remove("charlie")

    assert registry.get("charlie") is None


def test_exists():

    registry = UserRegistry()

    registry.register(
        User(
            username="david",
            role="viewer",
        )
    )

    assert registry.exists("david")

    assert not registry.exists("unknown")


def test_clear_registry():

    registry = UserRegistry()

    registry.register(
        User(
            username="alice",
            role="admin",
        )
    )

    registry.register(
        User(
            username="bob",
            role="researcher",
        )
    )

    registry.clear()

    assert registry.count() == 0
