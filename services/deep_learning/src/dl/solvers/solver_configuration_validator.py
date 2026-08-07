"""
RNAOS solver configuration validation.
"""

from __future__ import annotations

from dl.models.optimization.solver_configuration import (
    SolverConfiguration,
)


class SolverConfigurationValidator:
    """
    Validates solver configurations.
    """

    def validate(
        self,
        config: SolverConfiguration,
    ) -> bool:
        """
        Validate configuration.
        """

        if config.iterations <= 0:
            raise ValueError(
                "Iterations must be positive",
            )

        if config.initial_temperature <= 0:
            raise ValueError(
                "Temperature must be positive",
            )

        if not (0 < config.cooling_rate < 1):
            raise ValueError(
                "Cooling rate must be between 0 and 1",
            )

        if config.checkpoint_interval <= 0:
            raise ValueError(
                "Checkpoint interval must be positive",
            )

        return True
