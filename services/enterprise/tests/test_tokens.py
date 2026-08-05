from datetime import timedelta

from enterprise.security import TokenManager


def test_generate_token():

    manager = TokenManager()

    token = manager.generate("alice")

    assert token.username == "alice"

    assert manager.count() == 1


def test_validate_token():

    manager = TokenManager()

    token = manager.generate("alice")

    assert manager.validate(token.token)


def test_revoke_token():

    manager = TokenManager()

    token = manager.generate("alice")

    assert manager.revoke(token.token)

    assert not manager.validate(token.token)


def test_unknown_token():

    manager = TokenManager()

    assert not manager.validate("unknown")


def test_expired_token():

    manager = TokenManager()

    token = manager.generate(
        "alice",
        lifetime=timedelta(seconds=-1),
    )

    assert not manager.validate(token.token)
