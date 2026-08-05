from rnaos_platform.events import (
    Event,
    EventBus,
    EventType,
)


def test_publish_event() -> None:
    bus = EventBus()

    received: list[Event] = []

    def handler(event: Event) -> None:
        received.append(event)

    bus.subscribe(
        EventType.EXPERIMENT_COMPLETED,
        handler,
    )

    bus.publish(
        Event(
            event_type=EventType.EXPERIMENT_COMPLETED,
            source="research",
            payload={
                "id": "exp-001",
            },
        ),
    )

    assert len(received) == 1
    assert received[0].payload["id"] == "exp-001"


def test_multiple_subscribers() -> None:
    bus = EventBus()

    counter: list[str] = []

    def handler(event: Event) -> None:
        counter.append(event.source)

    bus.subscribe(
        EventType.SOLVER_SELECTED,
        handler,
    )

    bus.subscribe(
        EventType.SOLVER_SELECTED,
        handler,
    )

    bus.publish(
        Event(
            event_type=EventType.SOLVER_SELECTED,
            source="solver",
        ),
    )

    assert len(counter) == 2


def test_unsubscribe() -> None:
    bus = EventBus()

    called = []

    def handler(event: Event) -> None:
        called.append(True)

    bus.subscribe(
        EventType.RNA_LOADED,
        handler,
    )

    bus.unsubscribe(
        EventType.RNA_LOADED,
        handler,
    )

    bus.publish(
        Event(
            event_type=EventType.RNA_LOADED,
            source="research",
        ),
    )

    assert called == []


def test_subscriber_count() -> None:
    bus = EventBus()

    bus.subscribe(
        EventType.RNA_LOADED,
        lambda event: None,
    )

    assert (
        bus.subscriber_count(
            EventType.RNA_LOADED,
        )
        == 1
    )


def test_published_count() -> None:
    bus = EventBus()

    bus.publish(
        Event(
            event_type=EventType.RNA_VALIDATED,
            source="research",
        ),
    )

    assert bus.published_count() == 1


def test_history() -> None:
    bus = EventBus()

    event = Event(
        event_type=EventType.RNA_VALIDATED,
        source="research",
    )

    bus.publish(event)

    history = bus.history()

    assert len(history) == 1
    assert history[0] == event


def test_registered_events() -> None:
    bus = EventBus()

    bus.subscribe(
        EventType.RNA_LOADED,
        lambda event: None,
    )

    bus.subscribe(
        EventType.EXPERIMENT_COMPLETED,
        lambda event: None,
    )

    registered = bus.registered_events()

    assert EventType.RNA_LOADED in registered
    assert EventType.EXPERIMENT_COMPLETED in registered


def test_clear() -> None:
    bus = EventBus()

    bus.subscribe(
        EventType.RNA_LOADED,
        lambda event: None,
    )

    bus.publish(
        Event(
            event_type=EventType.RNA_LOADED,
            source="research",
        ),
    )

    bus.clear()

    assert (
        bus.subscriber_count(
            EventType.RNA_LOADED,
        )
        == 0
    )

    assert bus.published_count() == 0

    assert bus.history() == ()
