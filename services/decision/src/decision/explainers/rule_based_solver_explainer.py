from __future__ import annotations

from optimization.models.optimization_problem import (
    QUBOProblem,
)
from solver.base.base_solver import (
    BaseSolver,
)

from decision.confidence import (
    ConfidenceEngine,
)
from decision.explainers.solver_explainer import (
    SolverExplainer,
)
from decision.models import (
    DecisionReason,
    Evidence,
    Explanation,
)


class RuleBasedSolverExplainer(SolverExplainer):
    """
    Rule-based implementation of the SolverExplainer.

    This explainer generates structured explanations for solver
    recommendations using deterministic rules. It serves as the
    baseline explainability engine for RNAOS and can later be
    extended or complemented by machine learning and LLM-based
    explainers.
    """

    _FAMILY_ALTERNATIVES = {
        "exact": [
            "Exact Solver",
        ],
        "mathematical": [
            "Branch and Bound",
            "Mixed Integer Programming",
        ],
        "classical": [
            "Genetic Algorithm",
            "Simulated Annealing",
            "Tabu Search",
        ],
        "digital_annealer": [
            "Digital Annealer",
        ],
        "quantum": [
            "QAOA",
            "Quantum Annealing",
        ],
        "hybrid": [
            "Hybrid Quantum-Classical",
        ],
    }

    _FAMILY_TRADEOFFS = {
        "exact": [
            "Guarantees globally optimal solutions.",
            "Computational cost grows exponentially with problem size.",
            "Best suited for small optimization problems.",
        ],
        "mathematical": [
            "Provides mathematically rigorous optimization.",
            "Often produces high-quality solutions.",
            "Can become computationally expensive for very large problems.",
        ],
        "classical": [
            "Scales well to large optimization problems.",
            "Produces high-quality approximate solutions.",
            "Does not guarantee globally optimal solutions.",
        ],
        "digital_annealer": [
            "Designed for large combinatorial optimization problems.",
            "Provides fast annealing-based optimization.",
            "Requires specialized hardware or services.",
        ],
        "quantum": [
            "Can explore complex optimization landscapes.",
            "Promising for future large-scale optimization.",
            "Current quantum hardware availability is limited.",
        ],
        "hybrid": [
            "Combines strengths of multiple optimization paradigms.",
            "Improves robustness and scalability.",
            "Typically requires additional computational resources.",
        ],
    }

    def __init__(self) -> None:
        self._confidence = ConfidenceEngine()

    def explain(
        self,
        problem: QUBOProblem,
        solver: BaseSolver,
        alternatives: list[BaseSolver],
    ) -> Explanation:
        """
        Generate an explanation for a solver recommendation.

        Parameters
        ----------
        problem:
            Optimization problem to explain.

        solver:
            Recommended solver.

        alternatives:
            Alternative solver candidates.

        Returns
        -------
        Explanation
            Structured explanation describing the recommendation.
        """

        reasons: list[DecisionReason] = []

        recommendation = solver.name

        problem_size = problem.size

        solver_family = solver.capabilities.solver_family.value

        qubo_density = problem.metadata.get(
            "qubo_density",
            0.5,
        )

        # ------------------------------------------------------------------
        # Problem size reasoning
        # ------------------------------------------------------------------

        if problem_size <= 20:
            description = (
                f"The optimization problem contains {problem_size} variables, "
                "making exact optimization computationally practical."
            )
            importance = 0.95

        elif problem_size <= 100:
            description = (
                f"The optimization problem contains {problem_size} variables, "
                "where high-quality classical optimization solvers typically "
                "provide the best balance between runtime and solution quality."
            )
            importance = 0.90

        else:
            description = (
                f"The optimization problem contains {problem_size} variables, "
                "making scalable classical or hybrid optimization approaches "
                "more suitable than exhaustive search."
            )
            importance = 0.95

        reasons.append(
            DecisionReason(
                title="Problem Size",
                description=description,
                importance=importance,
                evidence=[
                    Evidence(
                        name="Problem Size",
                        value=problem_size,
                        description="Number of optimization variables.",
                        source="OptimizationProfiler",
                        weight=importance,
                    )
                ],
            )
        )

        # ------------------------------------------------------------------
        # QUBO density reasoning
        # ------------------------------------------------------------------

        if qubo_density < 0.30:
            density_description = (
                f"The QUBO graph has a low density ({qubo_density:.2f}), "
                "indicating relatively weak interactions between variables. "
                "Sparse optimization problems are generally easier to solve."
            )
            density_importance = 0.70

        elif qubo_density < 0.70:
            density_description = (
                f"The QUBO graph has a moderate density ({qubo_density:.2f}), "
                "representing a balanced interaction structure that is well "
                "suited to many optimization algorithms."
            )
            density_importance = 0.80

        else:
            density_description = (
                f"The QUBO graph has a high density ({qubo_density:.2f}), "
                "indicating strong coupling between variables. Dense "
                "optimization problems generally benefit from robust "
                "classical optimization strategies."
            )
            density_importance = 0.90

        reasons.append(
            DecisionReason(
                title="QUBO Density",
                description=density_description,
                importance=density_importance,
                evidence=[
                    Evidence(
                        name="QUBO Density",
                        value=qubo_density,
                        description="Normalized QUBO graph density.",
                        source="QUBOGenerator",
                        weight=density_importance,
                    )
                ],
            )
        )

        # ------------------------------------------------------------------
        # Solver family reasoning
        # ------------------------------------------------------------------

        family = solver_family.lower()

        if family == "exact":
            family_description = (
                "The selected solver belongs to the Exact solver family. "
                "Exact algorithms guarantee globally optimal solutions but "
                "their computational cost increases rapidly with problem size."
            )
            family_importance = 0.95

        elif family == "mathematical":
            family_description = (
                "The selected solver belongs to the Mathematical optimization "
                "family. Mathematical programming methods exploit formal "
                "optimization models and deterministic search techniques."
            )
            family_importance = 0.90

        elif family == "classical":
            family_description = (
                "The selected solver belongs to the Classical optimization "
                "family. Classical optimization algorithms use heuristic and "
                "metaheuristic search strategies to efficiently explore "
                "large optimization spaces."
            )
            family_importance = 0.90

        elif family == "digital_annealer":
            family_description = (
                "The selected solver belongs to the Digital Annealer family. "
                "Digital annealing accelerates combinatorial optimization "
                "through specialized annealing hardware and algorithms."
            )
            family_importance = 0.92

        elif family == "quantum":
            family_description = (
                "The selected solver belongs to the Quantum optimization family. "
                "Quantum algorithms exploit quantum computational principles "
                "to explore complex optimization landscapes."
            )
            family_importance = 0.95

        elif family == "hybrid":
            family_description = (
                "The selected solver belongs to the Hybrid optimization family. "
                "Hybrid solvers combine multiple optimization paradigms to "
                "improve robustness, scalability, and solution quality."
            )
            family_importance = 0.90

        else:
            family_description = "The selected solver belongs to a specialized optimization family."
            family_importance = 0.70

        reasons.append(
            DecisionReason(
                title="Solver Family",
                description=family_description,
                importance=family_importance,
                evidence=[
                    Evidence(
                        name="Solver Family",
                        value=solver_family,
                        description="Classification of the recommended solver.",
                        source="SolverPortfolio",
                        weight=family_importance,
                    )
                ],
            )
        )

        # ------------------------------------------------------------------
        # Alternative solver recommendations
        # ------------------------------------------------------------------

        if alternatives:
            alternative_names = [
                candidate.name for candidate in alternatives if candidate.name != recommendation
            ]
        else:
            alternative_names = self._FAMILY_ALTERNATIVES.get(
                family,
                [],
            )

        # ------------------------------------------------------------------
        # Trade-off generation
        # ------------------------------------------------------------------

        tradeoffs = self._FAMILY_TRADEOFFS.get(
            family,
            [
                "Specialized optimization strategy.",
            ],
        )

        # ------------------------------------------------------------------
        # Confidence estimation
        # ------------------------------------------------------------------

        confidence = self._confidence.score(
            problem_size=problem_size,
            # Placeholder until solver validation metrics are available.
            relative_error=0.05,
            deterministic_solver=(solver.capabilities.deterministic),
        )

        return Explanation(
            recommendation=recommendation,
            confidence=confidence,
            reasons=reasons,
            alternatives=alternative_names,
            tradeoffs=tradeoffs,
            metadata={
                "problem_size": problem_size,
                "qubo_density": qubo_density,
                "solver_family": solver_family,
            },
        )
