"""
In-memory cache backend.
"""

from __future__ import annotations

from threading import RLock

from cloud.cache.cache_backend import CacheBackend
from cloud.cache.cache_entry import CacheEntry


class MemoryCacheBackend(CacheBackend):
    """Thread-safe in-memory cache backend."""

    def __init__(self) -> None:
        self._entries: dict[str, CacheEntry] = {}
        self._lock = RLock()

    def put(
        self,
        entry: CacheEntry,
    ) -> None:
        """Store a cache entry."""
        with self._lock:
            self._entries[entry.key] = entry

    def get(
        self,
        key: str,
    ) -> CacheEntry | None:
        """Retrieve a cache entry."""
        with self._lock:
            entry = self._entries.get(key)

            if entry is None:
                return None

            if entry.is_expired():
                self._entries.pop(key, None)
                return None

            return entry

    def remove(
        self,
        key: str,
    ) -> None:
        """Remove a cache entry."""
        with self._lock:
            self._entries.pop(key, None)

    def clear(
        self,
    ) -> None:
        """Clear all cache entries."""
        with self._lock:
            self._entries.clear()

    def count(
        self,
    ) -> int:
        """Return the number of cached entries."""
        with self._lock:
            return len(self._entries)

    def put_if_absent(
        self,
        entry: CacheEntry,
    ) -> bool:
        """
        Store the entry only if the key does not already exist.
        """
        with self._lock:
            if entry.key in self._entries:
                return False

            self._entries[entry.key] = entry
            return True

    def replace(
        self,
        entry: CacheEntry,
    ) -> bool:
        """
        Replace an existing cache entry.
        """
        with self._lock:
            if entry.key not in self._entries:
                return False

            self._entries[entry.key] = entry
            return True

    def compare_and_swap(
        self,
        key: str,
        expected_value: object,
        new_entry: CacheEntry,
    ) -> bool:
        """
        Atomically replace the cache entry if the current value
        matches the expected value.
        """
        with self._lock:
            current = self._entries.get(key)

            if current is None:
                return False

            if current.is_expired():
                self._entries.pop(key, None)
                return False

            if current.value != expected_value:
                return False

            self._entries[key] = new_entry
            return True
