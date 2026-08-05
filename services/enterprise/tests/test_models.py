from enterprise.security import (
    ApiToken,
    Permission,
    Role,
    Session,
    User,
    UserStatus,
)


def test_permission():

    permission = Permission("deploy")

    assert permission.name == "deploy"


def test_role_permission():

    role = Role("admin")

    role.add_permission("deploy")

    assert role.has_permission("deploy")


def test_user_defaults():

    user = User(
        username="alice",
        role="admin",
    )

    assert user.status == UserStatus.ACTIVE

    assert user.metadata == {}


def test_session():

    session = Session(
        session_id="session-1",
        username="alice",
    )

    assert session.username == "alice"


def test_api_token():

    token = ApiToken(
        token="abc123",
        username="alice",
    )

    assert token.username == "alice"

    assert not token.revoked
