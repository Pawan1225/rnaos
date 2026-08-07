"""
Tests for experiment configuration.
"""

from __future__ import annotations

from dl.models.benchmark.experiment_config import (
    ExperimentConfig,
)


def test_experiment_config() -> None:
    """
    Experiment configuration can be created.
    """

    config = ExperimentConfig(
        experiment_id="EXP_001",
        name="RNAOS_vs_ViennaRNA",
        version="1.0",
        methods=(
            "vienna_rna",
            "rnaos_hybrid",
        ),
        random_seed=42,
        hardware="Apple_M3",
        software="RNAOS_14.6",
        status="draft",
    )

    assert config.experiment_id == ("EXP_001")

    assert config.name == ("RNAOS_vs_ViennaRNA")

    assert (
        len(
            config.methods,
        )
        == 2
    )

    assert config.random_seed == 42

    assert config.status == ("draft")
