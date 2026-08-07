"""
RNAOS quantum-inspired configuration validator.
"""

from __future__ import annotations

from dl.models.optimization.quantum_inspired_configuration import (
    QuantumInspiredConfiguration,
)


class QuantumInspiredConfigurationValidator:
    """
    Validates quantum-inspired configuration.
    """

    def validate(
        self,
        config: QuantumInspiredConfiguration,
    ) -> bool:
        """
        Validate configuration.
        """

        if not (
            config.enable_qubo
            or config.enable_annealing
            or config.enable_tensor
            or config.enable_hybrid
        ):
            raise ValueError(
                "At least one optimizer must be enabled",
            )

        if config.seed < 0:
            raise ValueError(
                "Seed cannot be negative",
            )

        return True
