"""
RNAOS hybrid configuration validator.
"""

from __future__ import annotations

from dl.models.optimization.hybrid_configuration import (
    HybridConfiguration,
)


class HybridConfigurationValidator:
    """
    Validates hybrid optimization settings.
    """

    def validate(
        self,
        config: HybridConfiguration,
    ) -> bool:
        """
        Validate configuration.
        """

        if config.max_solvers <= 0:
            raise ValueError(
                "Maximum solvers must be positive",
            )

        if not (config.enable_qubo or config.enable_annealing or config.enable_tensor):
            raise ValueError(
                "At least one optimizer must be enabled",
            )

        return True
