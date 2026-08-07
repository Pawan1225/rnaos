"""
Tests for experiment configuration system.
"""

from __future__ import annotations

import pytest
from dl.benchmark.validation.experiment_validator import (
    ExperimentValidator,
)
from dl.models.benchmark.experiment_config import (
    ExperimentConfig,
)


@pytest.fixture
def validator() -> ExperimentValidator:
    """
    Create experiment validator.
    """

    return ExperimentValidator()


def create_valid_config() -> ExperimentConfig:
    """
    Create valid experiment configuration.
    """

    return ExperimentConfig(
        experiment_id="EXP_001",
        name="RNAOS_Benchmark",
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


def test_valid_configuration(
    validator: ExperimentValidator,
) -> None:
    """
    Valid configuration passes.
    """

    config = create_valid_config()

    assert validator.validate(
        config,
    )


def test_missing_methods(
    validator: ExperimentValidator,
) -> None:
    """
    Empty methods are rejected.
    """

    config = create_valid_config()

    invalid = ExperimentConfig(
        experiment_id=config.experiment_id,
        name=config.name,
        version=config.version,
        methods=(),
        random_seed=config.random_seed,
        hardware=config.hardware,
        software=config.software,
        status=config.status,
    )

    assert not validator.validate(
        invalid,
    )


def test_negative_seed(
    validator: ExperimentValidator,
) -> None:
    """
    Negative seed is rejected.
    """

    config = create_valid_config()

    invalid = ExperimentConfig(
        experiment_id=config.experiment_id,
        name=config.name,
        version=config.version,
        methods=config.methods,
        random_seed=-10,
        hardware=config.hardware,
        software=config.software,
        status=config.status,
    )

    assert not validator.validate(
        invalid,
    )


def test_invalid_status(
    validator: ExperimentValidator,
) -> None:
    """
    Unknown status is rejected.
    """

    config = create_valid_config()

    invalid = ExperimentConfig(
        experiment_id=config.experiment_id,
        name=config.name,
        version=config.version,
        methods=config.methods,
        random_seed=config.random_seed,
        hardware=config.hardware,
        software=config.software,
        status="unknown",
    )

    assert not validator.validate(
        invalid,
    )
