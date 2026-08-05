"""
RNAOS Event Bus.
"""

from __future__ import annotations

from collections import defaultdict, deque
from threading import RLock

from rnaos_platform.events.event import Event
from rnaos_platform.events.event_type import EventType
from rnaos_platform.events.subscriber import EventHandler


class EventBus:
    """Thread-safe publish/subscribe event bus."""

    def __init__(
        self,
        history_size: int = 1000,
    ) -> None:
        self._subscribers: dict[
            EventType,
            list[EventHandler],
        ] = defaultdict(list)

        self._history: deque[Event] = deque(
            maxlen=history_size,
        )

        self._published_count = 0

        self._lock = RLock()

    def subscribe(
        self,
        event_type: EventType,
        handler: EventHandler,
    ) -> None:
        """Register a subscriber."""

        with self._lock:
            self._subscribers[event_type].append(
                handler,
            )

    def unsubscribe(
        self,
        event_type: EventType,
        handler: EventHandler,
    ) -> None:
        """Remove a subscriber."""

        with self._lock:
            handlers = self._subscribers.get(
                event_type,
            )

            if handlers is None:
                return

            if handler in handlers:
                handlers.remove(handler)

            if not handlers:
                self._subscribers.pop(
                    event_type,
                    None,
                )

    def publish(
        self,
        event: Event,
    ) -> None:
        """Publish an event."""

        with self._lock:
            self._history.append(event)

            self._published_count += 1

            handlers = list(
                self._subscribers.get(
                    event.event_type,
                    [],
                ),
            )

        for handler in handlers:
            handler(event)

    def subscriber_count(
        self,
        event_type: EventType,
    ) -> int:
        """Return the number of subscribers."""

        with self._lock:
            return len(
                self._subscribers.get(
                    event_type,
                    [],
                ),
            )

    def published_count(
        self,
    ) -> int:
        """Return the total number of published events."""

        with self._lock:
            return self._published_count

    def history(
        self,
    ) -> tuple[Event, ...]:
        """Return published event history."""

        with self._lock:
            return tuple(self._history)

    def registered_events(
        self,
    ) -> tuple[EventType, ...]:
        """Return registered event types."""

        with self._lock:
            return tuple(
                sorted(
                    self._subscribers.keys(),
                    key=lambda event: event.value,
                ),
            )

    def clear(
        self,
    ) -> None:
        """Clear subscribers and event history."""

        with self._lock:
            self._subscribers.clear()

            self._history.clear()

            self._published_count = 0
