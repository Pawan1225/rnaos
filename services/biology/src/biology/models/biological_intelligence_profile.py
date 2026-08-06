"""
RNAOS biological intelligence profile.
"""

from __future__ import annotations

from dataclasses import dataclass

from biology.models.complexity_profile import (
    ComplexityProfile,
)
from biology.models.gc_content_features import (
    GCContentFeatures,
)
from biology.models.motif_profile import (
    MotifProfile,
)
from biology.models.sequence_features import (
    SequenceFeatures,
)
from biology.models.stem_loop_profile import (
    StemLoopProfile,
)
from biology.models.thermodynamic_profile import (
    ThermodynamicProfile,
)


@dataclass(slots=True, frozen=True)
class BiologicalIntelligenceProfile:
    """
    Unified biological intelligence profile.

    This profile aggregates the outputs of all biological
    analyzers into a single immutable object for downstream
    AI, machine learning, deep learning, quantum computing,
    and optimization workflows.
    """

    sequence: SequenceFeatures

    gc_content: GCContentFeatures

    complexity: ComplexityProfile

    motifs: MotifProfile

    stem_loops: StemLoopProfile

    thermodynamics: ThermodynamicProfile
