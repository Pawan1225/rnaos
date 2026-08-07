"""
RNAOS annealing profile generation engine.
"""

from __future__ import annotations

from dl.models.optimization.annealing_configuration import (
    AnnealingConfiguration,
)
from dl.models.optimization.annealing_profile import (
    AnnealingProfile,
)


class AnnealingProfileEngine:
    """
    Generates annealing intelligence profiles.
    """

    def generate(
        self,
        config: AnnealingConfiguration,
        algorithm: str,
        cooling_strategy: str,
        acceptance_strategy: str,
        restart_enabled: bool,
        convergence_threshold: float,
    ) -> AnnealingProfile:
        """
        Generate annealing profile.
        """

        return AnnealingProfile(
            algorithm=algorithm,
            initial_temperature=(config.initial_temperature),
            cooling_strategy=(cooling_strategy),
            acceptance_strategy=(acceptance_strategy),
            restart_enabled=(restart_enabled),
            convergence_threshold=(convergence_threshold),
        )
