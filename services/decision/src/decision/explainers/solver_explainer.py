from __future__ import annotations

from abc import ABC, abstractmethod

from decision.models import Explanation


class SolverExplainer(ABC):
    """
    Abstract base class for solver explanation engines.

    A SolverExplainer generates structured explanations describing
    why a particular optimization solver was recommended.

    Concrete implementations may use:
    - Rule-based reasoning
    - Historical benchmark data
    - Machine learning
    - Hybrid approaches
    - Future LLM-assisted reasoning

    All implementations must return a standardized Explanation object.
    """

    @abstractmethod
    def explain(self, *args, **kwargs) -> Explanation:
        """
        Generate an explanation for a solver recommendation.

        Returns
        -------
        Explanation
            Structured explanation describing the recommendation.
        """
        raise NotImplementedError
