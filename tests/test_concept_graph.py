import pytest

from src.models.concept_tree import ConceptIntegrityError, build_default_concept_graph


def test_default_graph_has_20_plus_concepts() -> None:
    g = build_default_concept_graph()
    assert len(g.nodes) >= 20


def test_learning_path_is_ordered_and_ends_with_target() -> None:
    g = build_default_concept_graph()
    target = "calc.integrals"
    path = g.learning_path_to(target)
    assert path[-1] == target
    # prereqs must appear before target
    prereqs = g.prerequisites_of(target)
    assert prereqs
    for p in prereqs:
        assert path.index(p) < path.index(target)


def test_integrity_detects_cycles() -> None:
    g = build_default_concept_graph()
    g.add_prerequisite(concept_id="arith.natural_numbers", prerequisite_id="calc.integrals")
    with pytest.raises(ConceptIntegrityError):
        g.validate_integrity()

