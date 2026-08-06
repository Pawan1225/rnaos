"""
RNAOS neural dataset engine.
"""

from __future__ import annotations

from dl.encoders.sequence_encoder import (
    RNASequenceEncoder,
)
from dl.encoders.structure_encoder import (
    RNAStructureEncoder,
)
from dl.encoders.thermodynamic_encoder import (
    RNAThermodynamicEncoder,
)
from dl.models.neural_dataset import (
    NeuralDataset,
)


class NeuralDatasetEngine:
    """
    Builds deep learning datasets from
    biological RNA representations.
    """

    def __init__(
        self,
    ) -> None:
        self.sequence_encoder = RNASequenceEncoder()

        self.structure_encoder = RNAStructureEncoder()

        self.thermodynamic_encoder = RNAThermodynamicEncoder()

    def build(
        self,
        sequence: str,
        structure: str,
        thermodynamic_features: tuple[float, ...],
        targets: tuple[float, ...],
    ) -> NeuralDataset:
        """
        Build a tensor-ready neural dataset.
        """

        sequence_tensor = (
            self.sequence_encoder.encode(
                sequence,
            ),
        )

        structure_tensor = (
            self.structure_encoder.encode(
                structure,
            ),
        )

        return NeuralDataset(
            sequence_tensors=sequence_tensor,
            structure_tensors=structure_tensor,
            thermodynamic_features=(thermodynamic_features),
            targets=targets,
            dataset_version="v1",
            sample_count=len(targets),
        )
