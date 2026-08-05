from enterprise.security import PasswordManager


def test_hash_password():

    manager = PasswordManager()

    password_hash = manager.hash_password("secret123")

    assert password_hash != "secret123"

    assert len(password_hash) == 64


def test_verify_password():

    manager = PasswordManager()

    password_hash = manager.hash_password("secret123")

    assert manager.verify_password(
        "secret123",
        password_hash,
    )


def test_verify_wrong_password():

    manager = PasswordManager()

    password_hash = manager.hash_password("secret123")

    assert not manager.verify_password(
        "wrong",
        password_hash,
    )
