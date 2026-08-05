"""
RNAOS event subscriber definitions.
"""

from __future__ import annotations

from collections.abc import Callable
from typing import TypeAlias

from rnaos_platform.events.event import Event

EventHandler: TypeAlias = Callable[
    [Event],
    None,
]
