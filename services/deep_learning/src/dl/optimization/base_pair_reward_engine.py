"""
RNAOS base pair reward engine.
"""

from __future__ import annotations

from dl.models.optimization.base_pair_reward import (
    BasePairReward,
)


class BasePairRewardEngine:
    """
    Provides biological pairing energies.
    """

    def calculate(
        self,
        pair_type: str,
    ) -> BasePairReward:
        """
        Return pairing energy.
        """

        rewards = {
            "GC": -3.0,
            "CG": -3.0,
            "AU": -2.0,
            "UA": -2.0,
            "GU": -1.0,
            "UG": -1.0,
        }

        if pair_type not in rewards:
            raise ValueError(
                "Unsupported base pair",
            )

        return BasePairReward(
            pair_type=pair_type,
            energy=rewards[pair_type],
        )
