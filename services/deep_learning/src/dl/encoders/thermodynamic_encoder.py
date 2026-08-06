"""
RNAOS RNA thermodynamic encoder.
"""

from __future__ import annotations

from dl.core.base_encoder import (
    BaseEncoder,
)


class RNAThermodynamicEncoder(BaseEncoder):
    """
    Encodes RNA thermodynamic features into
    neural representations.
    """

    def encode(
        self,
        inputs: tuple[float, ...],
    ) -> tuple[float, ...]:
        """
        Encode thermodynamic features.
        """

        return tuple(float(value) for value in inputs)

    def output_dimension(
        self,
    ) -> int:
        """
        Return dynamic thermodynamic dimension.

        Dimension depends on input features.
        """

        return 0

    def save(
        self,
        path: str,
    ) -> None:
        """
        Thermodynamic encoder has no parameters.
        """

        return None

    def load(
        self,
        path: str,
    ) -> None:
        """
        Thermodynamic encoder has no parameters.
        """

        return None
