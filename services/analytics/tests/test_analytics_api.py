from analytics.api import (
    AnalyticsAPI,
)
from analytics.digital_twin import (
    HealthStatus,
)
from analytics.models.experiment_record import (
    ExperimentRecord,
)


def test_api() -> None:
    api = AnalyticsAPI()

    api.add_experiment(
        ExperimentRecord(
            experiment_id="1",
            sequence="AAAA",
            solver="SA",
            objective_value=-10.0,
            runtime_seconds=0.20,
            confidence=0.90,
        )
    )

    assert len(api.get_history()) == 1

    performance = api.performance_summary()

    assert len(performance) == 1

    twin = api.build_digital_twin(
        benchmark_accuracy=0.95,
    )

    assert twin.total_experiments == 1

    assert twin.health == HealthStatus.HEALTHY


def test_api_methods() -> None:
    api = AnalyticsAPI()

    assert hasattr(
        api,
        "performance_summary",
    )

    assert hasattr(
        api,
        "runtime_trend",
    )

    assert hasattr(
        api,
        "recommendation",
    )

    assert hasattr(
        api,
        "build_digital_twin",
    )
