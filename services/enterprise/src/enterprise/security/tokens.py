"""
Token management for the RNAOS Enterprise Security Framework.
"""

from __future__ import annotations

import secrets
from datetime import UTC, datetime, timedelta

from enterprise.security.models import ApiToken


class TokenManager:
    """Manage API tokens."""

    def __init__(
        self,
    ) -> None:
        self._tokens: dict[str, ApiToken] = {}

    def generate(
        self,
        username: str,
        lifetime: timedelta | None = None,
    ) -> ApiToken:
        """Generate a new API token."""

        token = secrets.token_hex(32)

        created_at = datetime.now(UTC)

        expires_at = None

        if lifetime is not None:
            expires_at = created_at + lifetime

        api_token = ApiToken(
            token=token,
            username=username,
            created_at=created_at,
            expires_at=expires_at,
        )

        self._tokens[token] = api_token

        return api_token

    def get(
        self,
        token: str,
    ) -> ApiToken | None:
        """Retrieve a token."""

        return self._tokens.get(token)

    def validate(
        self,
        token: str,
    ) -> bool:
        """Validate a token."""

        api_token = self.get(token)

        if api_token is None:
            return False

        if api_token.revoked:
            return False

        return api_token.expires_at is None or datetime.now(UTC) < api_token.expires_at

    def revoke(
        self,
        token: str,
    ) -> bool:
        """Revoke a token."""

        api_token = self.get(token)

        if api_token is None:
            return False

        api_token.revoked = True

        return True

    def count(
        self,
    ) -> int:
        """Return the number of managed tokens."""

        return len(self._tokens)
