"""
Tests for RNAOS energy evaluator.
"""

from validation.energy.rnaos_energy_evaluator import (
    RNAOSEnergyEvaluator,
)


def test_rnaos_energy_evaluation():

    evaluator = RNAOSEnergyEvaluator()

    energy = evaluator.evaluate(
        "GGAGCAAAACUUGUCGAUUGAGAACAAAAUACAGAAUUUGCUUG",
        ".(((((((..((((...(((....)))...))))..))))))).",
    )

    assert isinstance(
        energy,
        float,
    )
