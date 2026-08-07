"""
Tests for scientific dashboard generator.
"""

from validation.dashboard.scientific_dashboard_generator import (
    ScientificDashboardGenerator,
)


def test_scientific_dashboard():

    generator = ScientificDashboardGenerator()

    dashboard = generator.generate()

    assert dashboard.dashboard_id == ("DASHBOARD_001")

    assert "accuracy" in dashboard.metrics

    assert "energy_gap" in dashboard.metrics

    assert dashboard.benchmark_version == ("1.0.0")
