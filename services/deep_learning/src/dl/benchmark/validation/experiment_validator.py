"""
RNAOS experiment configuration validator.
"""

from __future__ import annotations

from dl.models.benchmark.experiment_config import (
    ExperimentConfig,
)


class ExperimentValidator:
    """
    Validates scientific experiment definitions.
    """

    VALID_STATUSES = (
        "draft",
        "running",
        "completed",
    )

    def validate(
        self,
        config: ExperimentConfig,
    ) -> bool:
        """
        Validate experiment configuration.
        """

        if not config.experiment_id:
            return False

        if not config.name:
            return False

        if not config.version:
            return False

        if not config.methods:
            return False

        if config.random_seed < 0:
            return False

        return config.status in self.VALID_STATUSES
