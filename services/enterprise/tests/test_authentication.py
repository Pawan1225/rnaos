from enterprise.security import (
    AuthenticationManager,
    PasswordManager,
    User,
    UserRegistry,
)


def test_authenticate_username():

    registry = UserRegistry()

    registry.register(
        User(
            username="alice",
            role="admin",
        )
    )

    auth = AuthenticationManager(registry)

    assert auth.authenticate_username("alice")


def test_unknown_username():

    auth = AuthenticationManager(UserRegistry())

    assert not auth.authenticate_username("unknown")


def test_authenticate_password():

    registry = UserRegistry()

    registry.register(
        User(
            username="alice",
            role="admin",
        )
    )

    passwords = PasswordManager()

    password_hash = passwords.hash_password("secret123")

    auth = AuthenticationManager(
        registry,
        passwords,
    )

    assert auth.authenticate_password(
        "alice",
        "secret123",
        password_hash,
    )


def test_wrong_password():

    registry = UserRegistry()

    registry.register(
        User(
            username="alice",
            role="admin",
        )
    )

    passwords = PasswordManager()

    password_hash = passwords.hash_password("secret123")

    auth = AuthenticationManager(
        registry,
        passwords,
    )

    assert not auth.authenticate_password(
        "alice",
        "wrong",
        password_hash,
    )


def test_unknown_user_password():

    passwords = PasswordManager()

    auth = AuthenticationManager(
        UserRegistry(),
        passwords,
    )

    password_hash = passwords.hash_password("secret123")

    assert not auth.authenticate_password(
        "unknown",
        "secret123",
        password_hash,
    )
