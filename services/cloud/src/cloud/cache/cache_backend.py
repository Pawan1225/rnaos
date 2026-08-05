"""
Cache backend abstraction.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from cloud.cache.cache_entry import CacheEntry


class CacheBackend(ABC):
    """Abstract cache backend."""

    @abstractmethod
    def put(
        self,
        entry: CacheEntry,
    ) -> None:
        """Store a cache entry."""
        raise NotImplementedError

    @abstractmethod
    def get(
        self,
        key: str,
    ) -> CacheEntry | None:
        """Retrieve a cache entry by key."""
        raise NotImplementedError

    @abstractmethod
    def remove(
        self,
        key: str,
    ) -> None:
        """Remove a cache entry."""
        raise NotImplementedError

    @abstractmethod
    def clear(
        self,
    ) -> None:
        """Remove all cache entries."""
        raise NotImplementedError

    @abstractmethod
    def count(
        self,
    ) -> int:
        """Return the number of cached entries."""
        raise NotImplementedError

    @abstractmethod
    def put_if_absent(
        self,
        entry: CacheEntry,
    ) -> bool:
        """
        Store the entry only if the key does not already exist.

        Returns
        -------
        bool
            True if the entry was inserted, False otherwise.
        """
        raise NotImplementedError

    @abstractmethod
    def replace(
        self,
        entry: CacheEntry,
    ) -> bool:
        """
        Replace an existing cache entry.

        Returns
        -------
        bool
            True if the entry was replaced, False otherwise.
        """
        raise NotImplementedError

    @abstractmethod
    def compare_and_swap(
        self,
        key: str,
        expected_value: object,
        new_entry: CacheEntry,
    ) -> bool:
        """
        Atomically replace the cache entry if the current value matches.

        Returns
        -------
        bool
            True if the swap succeeded, False otherwise.
        """
        raise NotImplementedError
