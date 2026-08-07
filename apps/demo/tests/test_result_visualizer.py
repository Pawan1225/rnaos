"""
Tests for RNAOS result visualization.
"""

from apps.demo.visualization.result_visualizer import (
    ResultVisualizer,
)


class FakeResult:
    """
    Mock demo result.
    """

    sequence = "GGCAU"

    predicted_structure = "(((...)))"

    reference_structure = "(((...)))"

    accuracy = 1.0

    energy_gap = 0.0

    runtime = 0.1

    estimated_qubits = 10


def test_result_visualizer():

    visualizer = ResultVisualizer()

    report = visualizer.create_report(FakeResult())

    assert report.title == ("RNAOS Optimization Result")

    assert report.sequence == "GGCAU"

    assert report.accuracy == 1.0

    assert report.energy_gap == 0.0

    assert report.estimated_qubits == 10
