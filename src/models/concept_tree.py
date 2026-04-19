"""
Concept graph for mathematics learning.

- Nodes are concepts (Arithmetic/Algebra/Geometry/Calculus).
- Directed edges represent prerequisites: (A -> B) means A is a prerequisite of B.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone


class ConceptGraphError(Exception):
    pass


class ConceptIntegrityError(ConceptGraphError):
    pass


@dataclass(frozen=True)
class ConceptNode:
    concept_id: str
    name: str
    domain: str
    description: str = ""
    tags: frozenset[str] = field(default_factory=frozenset)


class ConceptGraph:
    """
    Directed graph where an edge (A -> B) means A is a prerequisite of B.
    """

    def __init__(self) -> None:
        self.nodes: dict[str, ConceptNode] = {}
        self._prereqs: dict[str, set[str]] = {}  # concept_id -> prerequisite_ids

    def add_concept(self, node: ConceptNode) -> None:
        if node.concept_id in self.nodes:
            raise ConceptGraphError(f"Duplicate concept_id: {node.concept_id}")
        self.nodes[node.concept_id] = node
        self._prereqs.setdefault(node.concept_id, set())

    def add_prerequisite(self, *, concept_id: str, prerequisite_id: str) -> None:
        if concept_id not in self.nodes:
            raise ConceptGraphError(f"Unknown concept_id: {concept_id}")
        if prerequisite_id not in self.nodes:
            raise ConceptGraphError(f"Unknown prerequisite_id: {prerequisite_id}")
        if concept_id == prerequisite_id:
            raise ConceptGraphError("A concept cannot be its own prerequisite.")
        self._prereqs.setdefault(concept_id, set()).add(prerequisite_id)

    def prerequisites_of(self, concept_id: str) -> set[str]:
        return set(self._prereqs.get(concept_id, set()))

    def dependents_of(self, prerequisite_id: str) -> set[str]:
        dependents: set[str] = set()
        for cid, prereqs in self._prereqs.items():
            if prerequisite_id in prereqs:
                dependents.add(cid)
        return dependents

    def find_by_name(self, name: str) -> list[ConceptNode]:
        needle = name.strip().lower()
        if not needle:
            return []
        return [n for n in self.nodes.values() if n.name.lower() == needle]

    def validate_integrity(self) -> None:
        missing: list[tuple[str, str]] = []
        for cid, prereqs in self._prereqs.items():
            if cid not in self.nodes:
                raise ConceptIntegrityError(f"Prereq table references unknown concept_id: {cid}")
            for pid in prereqs:
                if pid not in self.nodes:
                    missing.append((cid, pid))
        if missing:
            details = ", ".join([f"{c}->{p}" for c, p in missing[:10]])
            more = "" if len(missing) <= 10 else f" (+{len(missing) - 10} more)"
            raise ConceptIntegrityError(f"Missing prerequisite references: {details}{more}")

        self._raise_if_cycle()

    def _raise_if_cycle(self) -> None:
        visiting: set[str] = set()
        visited: set[str] = set()
        stack: list[str] = []

        def dfs(node_id: str) -> None:
            if node_id in visited:
                return
            if node_id in visiting:
                if node_id in stack:
                    i = stack.index(node_id)
                    cycle = stack[i:] + [node_id]
                    raise ConceptIntegrityError("Cycle detected: " + " -> ".join(cycle))
                raise ConceptIntegrityError(f"Cycle detected involving {node_id}")

            visiting.add(node_id)
            stack.append(node_id)
            for prereq in self._prereqs.get(node_id, set()):
                dfs(prereq)
            stack.pop()
            visiting.remove(node_id)
            visited.add(node_id)

        for cid in self.nodes.keys():
            dfs(cid)

    def learning_path_to(self, concept_id: str) -> list[str]:
        """
        Ordered prerequisite path ending with `concept_id`.
        """
        if concept_id not in self.nodes:
            raise ConceptGraphError(f"Unknown concept_id: {concept_id}")
        self.validate_integrity()

        ordered: list[str] = []
        seen: set[str] = set()

        def visit(cid: str) -> None:
            if cid in seen:
                return
            for prereq in sorted(self._prereqs.get(cid, set())):
                visit(prereq)
            seen.add(cid)
            ordered.append(cid)

        visit(concept_id)
        return ordered

    def to_dict(self) -> dict:
        now = datetime.now(timezone.utc).isoformat()
        concepts: dict[str, dict] = {}
        for cid, node in self.nodes.items():
            concepts[cid] = {
                "concept_id": node.concept_id,
                "name": node.name,
                "domain": node.domain,
                "description": node.description,
                "tags": sorted(node.tags),
                "prerequisites": sorted(self.prerequisites_of(cid)),
            }
        return {"schema_version": 1, "updated_at": now, "concepts": concepts}


def build_default_concept_graph() -> ConceptGraph:
    """
    Generates a graph with 20+ concepts across Arithmetic, Algebra, Geometry, Calculus.
    """
    g = ConceptGraph()

    def add(concept_id: str, name: str, domain: str, description: str) -> None:
        g.add_concept(ConceptNode(concept_id=concept_id, name=name, domain=domain, description=description))

    # Arithmetic (10)
    add("arith.natural_numbers", "Natural Numbers", "Arithmetic", "Counting numbers and their properties.")
    add("arith.integers", "Integers", "Arithmetic", "Whole numbers including negatives.")
    add("arith.fractions", "Fractions", "Arithmetic", "Parts of a whole; numerator and denominator.")
    add("arith.decimals", "Decimals", "Arithmetic", "Base-10 representation of fractions.")
    add("arith.addition", "Addition", "Arithmetic", "Combining quantities.")
    add("arith.subtraction", "Subtraction", "Arithmetic", "Finding differences.")
    add("arith.multiplication", "Multiplication", "Arithmetic", "Repeated addition and scaling.")
    add("arith.division", "Division", "Arithmetic", "Partitioning and ratios.")
    add("arith.order_of_operations", "Order of Operations", "Arithmetic", "Rules for evaluating expressions.")
    add("arith.exponents", "Exponents", "Arithmetic", "Repeated multiplication and powers.")

    # Algebra (7)
    add("alg.variables", "Variables", "Algebra", "Symbols representing unknown quantities.")
    add("alg.expressions", "Algebraic Expressions", "Algebra", "Combinations of numbers, variables, and operations.")
    add("alg.equations", "Equations", "Algebra", "Statements of equality between expressions.")
    add("alg.linear_equations", "Linear Equations", "Algebra", "Equations of the form ax + b = c.")
    add("alg.functions", "Functions", "Algebra", "Mappings from inputs to outputs.")
    add("alg.quadratics", "Quadratic Functions", "Algebra", "Functions of the form ax^2 + bx + c.")
    add("alg.polynomials", "Polynomials", "Algebra", "Expressions with multiple power terms.")

    # Geometry (6)
    add("geo.points_lines", "Points and Lines", "Geometry", "Basic geometric primitives.")
    add("geo.angles", "Angles", "Geometry", "Measures of rotation between rays.")
    add("geo.triangles", "Triangles", "Geometry", "Three-sided polygons and their properties.")
    add("geo.circles", "Circles", "Geometry", "Points equidistant from a center.")
    add("geo.area_perimeter", "Area and Perimeter", "Geometry", "Measuring size and boundary length.")
    add("geo.coordinate_plane", "Coordinate Plane", "Geometry", "Representing geometry with coordinates.")

    # Calculus (5)
    add("calc.limits", "Limits", "Calculus", "Values approached by functions.")
    add("calc.continuity", "Continuity", "Calculus", "When a function has no breaks.")
    add("calc.derivatives", "Derivatives", "Calculus", "Rates of change and slopes.")
    add("calc.integrals", "Integrals", "Calculus", "Accumulation and area under curves.")
    add("calc.series", "Series", "Calculus", "Sums of sequences of terms.")

    # Prerequisite edges (examples, enough to create meaningful paths)
    # Arithmetic foundations
    g.add_prerequisite(concept_id="arith.integers", prerequisite_id="arith.natural_numbers")
    g.add_prerequisite(concept_id="arith.addition", prerequisite_id="arith.natural_numbers")
    g.add_prerequisite(concept_id="arith.subtraction", prerequisite_id="arith.addition")
    g.add_prerequisite(concept_id="arith.multiplication", prerequisite_id="arith.addition")
    g.add_prerequisite(concept_id="arith.division", prerequisite_id="arith.multiplication")
    g.add_prerequisite(concept_id="arith.fractions", prerequisite_id="arith.division")
    g.add_prerequisite(concept_id="arith.decimals", prerequisite_id="arith.fractions")
    g.add_prerequisite(concept_id="arith.order_of_operations", prerequisite_id="arith.addition")
    g.add_prerequisite(concept_id="arith.order_of_operations", prerequisite_id="arith.multiplication")
    g.add_prerequisite(concept_id="arith.exponents", prerequisite_id="arith.multiplication")

    # Algebra
    g.add_prerequisite(concept_id="alg.variables", prerequisite_id="arith.natural_numbers")
    g.add_prerequisite(concept_id="alg.expressions", prerequisite_id="alg.variables")
    g.add_prerequisite(concept_id="alg.expressions", prerequisite_id="arith.order_of_operations")
    g.add_prerequisite(concept_id="alg.equations", prerequisite_id="alg.expressions")
    g.add_prerequisite(concept_id="alg.linear_equations", prerequisite_id="alg.equations")
    g.add_prerequisite(concept_id="alg.polynomials", prerequisite_id="alg.expressions")
    g.add_prerequisite(concept_id="alg.functions", prerequisite_id="alg.expressions")
    g.add_prerequisite(concept_id="alg.quadratics", prerequisite_id="alg.functions")
    g.add_prerequisite(concept_id="alg.quadratics", prerequisite_id="alg.polynomials")

    # Geometry
    g.add_prerequisite(concept_id="geo.angles", prerequisite_id="geo.points_lines")
    g.add_prerequisite(concept_id="geo.triangles", prerequisite_id="geo.angles")
    g.add_prerequisite(concept_id="geo.circles", prerequisite_id="geo.angles")
    g.add_prerequisite(concept_id="geo.coordinate_plane", prerequisite_id="arith.integers")
    g.add_prerequisite(concept_id="geo.coordinate_plane", prerequisite_id="geo.points_lines")
    g.add_prerequisite(concept_id="geo.area_perimeter", prerequisite_id="arith.multiplication")
    g.add_prerequisite(concept_id="geo.area_perimeter", prerequisite_id="geo.triangles")

    # Calculus
    g.add_prerequisite(concept_id="calc.limits", prerequisite_id="alg.functions")
    g.add_prerequisite(concept_id="calc.continuity", prerequisite_id="calc.limits")
    g.add_prerequisite(concept_id="calc.derivatives", prerequisite_id="calc.limits")
    g.add_prerequisite(concept_id="calc.integrals", prerequisite_id="calc.derivatives")
    g.add_prerequisite(concept_id="calc.series", prerequisite_id="arith.exponents")

    g.validate_integrity()
    return g


def build_math_concept_tree() -> ConceptGraph:
    """
    Backwards-friendly name: returns the default prerequisite graph.
    """
    return build_default_concept_graph()

