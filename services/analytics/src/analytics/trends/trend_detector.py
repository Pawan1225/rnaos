"""
Trend detection for RNAOS analytics.
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from enum import StrEnum
from statistics import mean

from analytics.models.experiment_record import ExperimentRecord


class TrendDirection(StrEnum):
    """Trend direction."""

    IMPROVING = "IMPROVING"
    STABLE = "STABLE"
    REGRESSING = "REGRESSING"


@dataclass(slots=True)
class Trend:
    """Represents a detected trend."""

    metric: str
    direction: TrendDirection
    previous: float
    current: float
    delta: float
    percent_change: float


class TrendDetector:
    """Detect trends in historical experiment data."""

    def detect_runtime(
        self,
        records: list[ExperimentRecord],
    ) -> Trend | None:
        return self._detect(
            records,
            "runtime",
            lambda record: record.runtime_seconds,
            lower_is_better=True,
        )

    def detect_confidence(
        self,
        records: list[ExperimentRecord],
    ) -> Trend | None:
        return self._detect(
            records,
            "confidence",
            lambda record: record.confidence,
            lower_is_better=False,
        )

    def detect_objective(
        self,
        records: list[ExperimentRecord],
    ) -> Trend | None:
        return self._detect(
            records,
            "objective",
            lambda record: record.objective_value,
            lower_is_better=True,
        )

    def _detect(
        self,
        records: list[ExperimentRecord],
        metric: str,
        extractor: Callable[[ExperimentRecord], float],
        *,
        lower_is_better: bool,
    ) -> Trend | None:
        """Detect the trend for a single metric."""

        if len(records) < 2:
            return None

        # The newer half intentionally receives the extra
        # sample when the history length is odd.
        midpoint = len(records) // 2

        previous_records = records[:midpoint]
        current_records = records[midpoint:]

        previous = mean(extractor(record) for record in previous_records)

        current = mean(extractor(record) for record in current_records)

        delta = current - previous

        percent = (delta / abs(previous)) * 100 if previous != 0 else 0.0

        tolerance = 1e-9

        if abs(delta) <= tolerance:
            direction = TrendDirection.STABLE
        elif lower_is_better:
            direction = (
                TrendDirection.IMPROVING if current < previous else TrendDirection.REGRESSING
            )
        else:
            direction = (
                TrendDirection.IMPROVING if current > previous else TrendDirection.REGRESSING
            )

        return Trend(
            metric=metric,
            direction=direction,
            previous=previous,
            current=current,
            delta=delta,
            percent_change=percent,
        )
