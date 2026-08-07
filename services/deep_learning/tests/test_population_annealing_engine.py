"""
Tests for population annealing engine.
"""

from __future__ import annotations

from dl.models.optimization.annealing_population import (
    AnnealingPopulation,
)
from dl.models.optimization.population_annealing_result import (
    PopulationAnnealingResult,
)
from dl.models.optimization.population_candidate import (
    PopulationCandidate,
)
from dl.optimization.population_annealing_engine import (
    PopulationAnnealingEngine,
)


def test_population_annealing() -> None:
    """
    Best candidate is selected.
    """

    population = AnnealingPopulation(
        candidates=(
            PopulationCandidate(
                candidate_id=1,
                state=(),
                energy=-5.0,
                fitness=0.5,
            ),
            PopulationCandidate(
                candidate_id=2,
                state=(),
                energy=-10.0,
                fitness=0.95,
            ),
        ),
        temperature=10.0,
        generation=1,
    )

    engine = PopulationAnnealingEngine()

    result = engine.optimize(
        population,
        generations=5,
    )

    assert isinstance(
        result,
        PopulationAnnealingResult,
    )

    assert result.best_candidate.candidate_id == 2

    assert result.generations == 5

    assert result.final_temperature == 2.0

    assert result.converged is True
