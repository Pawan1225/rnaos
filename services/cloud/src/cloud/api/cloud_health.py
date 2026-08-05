"""
RNAOS Cloud health model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class CloudHealth:
    """Overall cloud platform health."""

    execution: bool = True

    scheduler: bool = True

    queue: bool = True

    artifacts: bool = True

    cache: bool = True

    cluster: bool = True

    @property
    def healthy(
        self,
    ) -> bool:
        """Return overall platform health."""

        return all(
            (
                self.execution,
                self.scheduler,
                self.queue,
                self.artifacts,
                self.cache,
                self.cluster,
            )
        )

    @property
    def unhealthy_services(
        self,
    ) -> list[str]:
        """Return names of unhealthy services."""

        services: list[str] = []

        if not self.execution:
            services.append("execution")

        if not self.scheduler:
            services.append("scheduler")

        if not self.queue:
            services.append("queue")

        if not self.artifacts:
            services.append("artifacts")

        if not self.cache:
            services.append("cache")

        if not self.cluster:
            services.append("cluster")

        return services
