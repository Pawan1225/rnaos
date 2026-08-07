"""
Tests for RNAOS energy aware optimizer.
"""

from validation.optimization.energy_aware_optimizer import (
    EnergyAwareOptimizer,
)


class MockGenerator:
    """
    Generates candidate structures.
    """

    def generate(
        self,
        sequence: str,
    ) -> tuple[str, ...]:

        return (
            ".........",
            "(((...)))",
        )


class MockValidator:
    """
    Validates structures.
    """

    def validate(
        self,
        sequence: str,
        structure: str,
    ) -> bool:

        return True


class MockEvaluator:
    """
    Evaluates structure energy.
    """

    def evaluate(
        self,
        sequence: str,
        structure: str,
    ) -> float:

        if structure == "(((...)))":
            return -5.0

        return 0.0


def test_energy_optimizer_selects_best():

    optimizer = EnergyAwareOptimizer(
        generator=MockGenerator(),
        validator=MockValidator(),
        evaluator=MockEvaluator(),
    )

    result = optimizer.optimize(
        "GGGAAACCC",
    )

    assert result == "(((...)))"
