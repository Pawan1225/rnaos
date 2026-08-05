"""
Cache statistics.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class CacheStatistics:
    """Runtime cache statistics."""

    hits: int = 0

    misses: int = 0

    @property
    def requests(self) -> int:
        """Total cache requests."""
        return self.hits + self.misses

    @property
    def hit_ratio(self) -> float:
        """Cache hit ratio."""
        if self.requests == 0:
            return 0.0

        return self.hits / self.requests
