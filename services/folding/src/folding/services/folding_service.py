from folding.interfaces.folding_engine import FoldingEngine


class FoldingService:
    """
    Central orchestration service for RNA folding.

    This service provides a unified interface to RNA folding
    engines and related biological analysis components.
    """

    def __init__(self, engine: FoldingEngine):
        """
        Initialize the folding service.

        Parameters
        ----------
        engine : FoldingEngine
            Folding backend implementation.
        """
        self.engine = engine

    def fold(self, sequence: str):
        """
        Predict the secondary structure of an RNA sequence.
        """
        return self.engine.fold(sequence)

    def mfe(self, sequence: str) -> float:
        """
        Compute the minimum free energy (MFE) of an RNA sequence.
        """
        return self.engine.mfe(sequence)
