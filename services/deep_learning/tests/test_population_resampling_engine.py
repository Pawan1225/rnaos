"""
Tests for population resampling engine.
"""

from __future__ import annotations

from dl.models.optimization.annealing_population import (
    AnnealingPopulation,
)
from dl.models.optimization.population_candidate import (
    PopulationCandidate,
)
from dl.models.optimization.resampling_result import (
    ResamplingResult,
)
from dl.optimization.population_resampling_engine import (
    PopulationResamplingEngine,
)


def test_population_resampling() -> None:
    """
    Strongest candidates are selected.
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
                fitness=0.9,
            ),
        ),
        temperature=5.0,
        generation=1,
    )

    engine = PopulationResamplingEngine()

    result = engine.resample(
        population,
        size=1,
    )

    assert isinstance(
        result,
        ResamplingResult,
    )

    assert (
        len(
            result.selected,
        )
        == 1
    )

    assert result.selected[0].candidate_id == 2

    assert result.removed_count == 1

    assert result.generation == 2
