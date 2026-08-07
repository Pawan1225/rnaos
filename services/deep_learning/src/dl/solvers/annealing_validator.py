"""
RNAOS annealing configuration validator.
"""

from __future__ import annotations

from dl.models.optimization.annealing_configuration import (
    AnnealingConfiguration,
)


class AnnealingConfigurationValidator:
    """
    Validates annealing parameters.
    """

    def validate(
        self,
        config: AnnealingConfiguration,
    ) -> bool:
        """
        Validate configuration.
        """

        if config.initial_temperature <= 0:
            raise ValueError(
                "Initial temperature must be positive",
            )

        if config.minimum_temperature < 0:
            raise ValueError(
                "Minimum temperature cannot be negative",
            )

        if not (0 < config.cooling_rate < 1):
            raise ValueError(
                "Cooling rate must be between 0 and 1",
            )

        if config.iterations <= 0:
            raise ValueError(
                "Iterations must be positive",
            )

        return True
