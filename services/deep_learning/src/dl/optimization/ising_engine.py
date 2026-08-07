"""
RNAOS Ising conversion engine.
"""

from __future__ import annotations

from dl.models.optimization.ising_model import (
    IsingModel,
)
from dl.models.optimization.qubo_model import (
    QUBOModel,
)


class IsingEngine:
    """
    Converts optimization problems
    into Ising representation.
    """

    def from_qubo(
        self,
        model: QUBOModel,
    ) -> IsingModel:
        """
        Convert QUBO to Ising form.

        Initial implementation keeps
        equivalent interaction structure.
        """

        size = len(
            model.variables,
        )

        fields = tuple(0.0 for _ in range(size))

        return IsingModel(
            variables=model.variables,
            local_fields=fields,
            couplings=model.matrix,
            offset=model.offset,
        )
