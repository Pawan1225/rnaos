"""
Tests for RNAOS experiment runner.
"""

from validation.runners.rnaos_experiment_runner import (
    RNAOSExperimentRunner,
)


def test_rnaos_execution() -> None:
    """
    RNAOS execution returns result.
    """

    runner = RNAOSExperimentRunner()

    result = runner.run(
        "AUGCUAGCUA",
    )

    assert result.version == ("1.0.0")

    assert result.solver == ("hybrid_quantum_inspired")

    assert result.qubit_estimate == 10

    assert result.variable_count == 20
