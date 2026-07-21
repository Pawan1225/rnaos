import pytest
from rna_intelligence.profilers.rna_profiler import RNAProfiler


@pytest.fixture
def rna_profile():
    """Reusable RNA profile for AI Intelligence tests."""
    return RNAProfiler().profile("GGGAAAUCC")
