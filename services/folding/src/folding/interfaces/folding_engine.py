from abc import ABC, abstractmethod


class FoldingEngine(ABC):
    """
    Abstract interface for RNA folding engines.

    Every folding backend (ViennaRNA, RNAstructure,
    LinearFold, etc.) must implement this interface.
    """

    @abstractmethod
    def fold(self, sequence: str):
        """
        Predict the secondary structure for an RNA sequence.

        Parameters
        ----------
        sequence : str
            RNA sequence.

        Returns
        -------
        object
            Engine-specific folding result.
        """
        raise NotImplementedError

    @abstractmethod
    def mfe(self, sequence: str) -> float:
        """
        Compute the minimum free energy (MFE).

        Parameters
        ----------
        sequence : str
            RNA sequence.

        Returns
        -------
        float
            Minimum free energy (kcal/mol).
        """
        raise NotImplementedError
