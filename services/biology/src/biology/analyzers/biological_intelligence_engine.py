"""
RNAOS biological intelligence engine.
"""

from __future__ import annotations

from biology.analyzers.complexity_analyzer import (
    ComplexityAnalyzer,
)
from biology.analyzers.gc_content_analyzer import (
    GCContentAnalyzer,
)
from biology.analyzers.motif_detector import (
    MotifDetector,
)
from biology.analyzers.sequence_analyzer import (
    SequenceAnalyzer,
)
from biology.analyzers.stem_loop_detector import (
    StemLoopDetector,
)
from biology.analyzers.thermodynamic_feature_extractor import (
    ThermodynamicFeatureExtractor,
)
from biology.models.biological_intelligence_profile import (
    BiologicalIntelligenceProfile,
)
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


class BiologicalIntelligenceEngine:
    """
    Unified entry point for biological intelligence.

    Architecture
    ------------
    Facade over the Biology service.

    Complexity
    ----------
    Time Complexity: O(n)

    The engine delegates computation to specialized
    analyzers and aggregates their outputs into a
    single immutable biological intelligence profile.

    This engine orchestrates all biological analyzers and
    returns a single immutable biological intelligence
    profile.
    """

    def __init__(
        self,
        *,
        sequence_analyzer: SequenceAnalyzer | None = None,
        gc_analyzer: GCContentAnalyzer | None = None,
        complexity_analyzer: ComplexityAnalyzer | None = None,
        motif_detector: MotifDetector | None = None,
        stem_loop_detector: StemLoopDetector | None = None,
        thermodynamic_extractor: (ThermodynamicFeatureExtractor | None) = None,
    ) -> None:
        self.sequence_analyzer = sequence_analyzer or SequenceAnalyzer()

        self.gc_analyzer = gc_analyzer or GCContentAnalyzer()

        self.complexity_analyzer = complexity_analyzer or ComplexityAnalyzer()

        self.motif_detector = motif_detector or MotifDetector()

        self.stem_loop_detector = stem_loop_detector or StemLoopDetector()

        self.thermodynamic_extractor = thermodynamic_extractor or ThermodynamicFeatureExtractor()

    def _build_profile(
        self,
        *,
        sequence_features: SequenceFeatures,
        gc_features: GCContentFeatures,
        complexity: ComplexityProfile,
        motifs: MotifProfile,
        stem_loops: StemLoopProfile,
        thermodynamics: ThermodynamicProfile,
    ) -> BiologicalIntelligenceProfile:
        """
        Build a biological intelligence profile.
        """
        return BiologicalIntelligenceProfile(
            sequence=sequence_features,
            gc_content=gc_features,
            complexity=complexity,
            motifs=motifs,
            stem_loops=stem_loops,
            thermodynamics=thermodynamics,
        )

    def analyze(
        self,
        sequence: str,
    ) -> BiologicalIntelligenceProfile:
        """
        Perform complete biological intelligence analysis.
        """
        if not sequence:
            raise ValueError("RNA sequence cannot be empty.")

        sequence_features = self.sequence_analyzer.analyze(
            sequence,
        )

        gc_features = self.gc_analyzer.analyze(
            sequence_features,
        )

        complexity = self.complexity_analyzer.analyze(
            sequence_features,
        )

        motifs = self.motif_detector.analyze(
            sequence_features,
        )

        stem_loops = self.stem_loop_detector.analyze(
            sequence_features,
        )

        thermodynamics = self.thermodynamic_extractor.analyze(
            sequence_features,
            gc_features,
            stem_loops,
        )

        return self._build_profile(
            sequence_features=sequence_features,
            gc_features=gc_features,
            complexity=complexity,
            motifs=motifs,
            stem_loops=stem_loops,
            thermodynamics=thermodynamics,
        )
