"""
Unified Analytics API.
"""

from __future__ import annotations

from analytics.digital_twin import (
    DigitalTwin,
    DigitalTwinBuilder,
)
from analytics.history import (
    ExperimentHistory,
)
from analytics.models.experiment_record import (
    ExperimentRecord,
)
from analytics.performance import (
    PerformanceAnalyzer,
    SolverPerformance,
)
from analytics.recommendation import (
    RecommendationEngine,
    SolverRecommendation,
)
from analytics.trends import (
    Trend,
    TrendDetector,
)


class AnalyticsAPI:
    """Unified entry point for RNAOS analytics."""

    def __init__(
        self,
        history: ExperimentHistory | None = None,
    ) -> None:

        self.history = history if history is not None else ExperimentHistory()

        self.performance = PerformanceAnalyzer()

        self.trends = TrendDetector()

        self.recommendations = RecommendationEngine()

        self.digital_twin = DigitalTwinBuilder()

    def add_experiment(
        self,
        record: ExperimentRecord,
    ) -> None:
        """Store an experiment."""
        self.history.add(record)

    def get_history(
        self,
    ) -> list[ExperimentRecord]:
        """Return all experiments."""
        return self.history.all()

    def performance_summary(
        self,
    ) -> list[SolverPerformance]:
        """Return solver performance summary."""
        return self.performance.summarize(self.history.all())

    def runtime_trend(
        self,
    ) -> Trend | None:
        """Return runtime trend."""
        return self.trends.detect_runtime(self.history.all())

    def confidence_trend(
        self,
    ) -> Trend | None:
        """Return confidence trend."""
        return self.trends.detect_confidence(self.history.all())

    def recommendation(
        self,
    ) -> SolverRecommendation:
        """Return solver recommendation."""
        return self.recommendations.recommend(self.performance_summary())

    def build_digital_twin(
        self,
        benchmark_accuracy: float,
    ) -> DigitalTwin:
        """Build the current Digital Twin."""

        performance = self.performance_summary()

        return self.digital_twin.build(
            records=self.history.all(),
            performance=performance,
            benchmark_accuracy=benchmark_accuracy,
        )
