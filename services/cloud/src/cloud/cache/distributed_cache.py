"""
RNAOS Distributed Cache.
"""

from __future__ import annotations

from typing import Any

from cloud.cache.cache_backend import CacheBackend
from cloud.cache.cache_entry import CacheEntry
from cloud.cache.cache_statistics import CacheStatistics
from cloud.cache.memory_cache_backend import (
    MemoryCacheBackend,
)


class DistributedCache:
    """Public interface for RNAOS distributed caching."""

    def __init__(
        self,
        backend: CacheBackend | None = None,
    ) -> None:
        self._backend = backend if backend is not None else MemoryCacheBackend()

        self._statistics = CacheStatistics()

    def _qualified_key(
        self,
        namespace: str,
        key: str,
    ) -> str:
        """Build a fully qualified cache key."""
        return f"{namespace}:{key}"

    def put(
        self,
        key: str,
        value: Any,
        ttl: int | None = None,
        namespace: str = "default",
    ) -> None:
        """Store a value in the cache."""

        entry = CacheEntry(
            key=self._qualified_key(
                namespace,
                key,
            ),
            value=value,
            ttl=ttl,
        )

        self._backend.put(entry)

    def get(
        self,
        key: str,
        namespace: str = "default",
    ) -> Any | None:
        """Retrieve a cached value."""

        entry = self._backend.get(
            self._qualified_key(
                namespace,
                key,
            )
        )

        if entry is None:
            self._statistics.misses += 1
            return None

        self._statistics.hits += 1

        return entry.value

    def remove(
        self,
        key: str,
        namespace: str = "default",
    ) -> None:
        """Remove a cached value."""

        self._backend.remove(
            self._qualified_key(
                namespace,
                key,
            )
        )

    def clear(
        self,
    ) -> None:
        """Clear the cache."""

        self._backend.clear()

    def count(
        self,
    ) -> int:
        """Return the number of cached entries."""

        return self._backend.count()

    def statistics(
        self,
    ) -> CacheStatistics:
        """Return cache statistics."""

        return self._statistics

    def put_if_absent(
        self,
        key: str,
        value: Any,
        ttl: int | None = None,
        namespace: str = "default",
    ) -> bool:
        """Store only if the key is absent."""

        return self._backend.put_if_absent(
            CacheEntry(
                key=self._qualified_key(
                    namespace,
                    key,
                ),
                value=value,
                ttl=ttl,
            )
        )

    def replace(
        self,
        key: str,
        value: Any,
        ttl: int | None = None,
        namespace: str = "default",
    ) -> bool:
        """Replace an existing cache entry."""

        return self._backend.replace(
            CacheEntry(
                key=self._qualified_key(
                    namespace,
                    key,
                ),
                value=value,
                ttl=ttl,
            )
        )

    def compare_and_swap(
        self,
        key: str,
        expected_value: Any,
        new_value: Any,
        ttl: int | None = None,
        namespace: str = "default",
    ) -> bool:
        """Atomically replace a cache value."""

        qualified_key = self._qualified_key(
            namespace,
            key,
        )

        return self._backend.compare_and_swap(
            qualified_key,
            expected_value,
            CacheEntry(
                key=qualified_key,
                value=new_value,
                ttl=ttl,
            ),
        )
