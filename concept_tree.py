"""
Legacy entry point for the concept tree.

The canonical implementation now lives at `src/models/concept_tree.py`.
This file stays for backward compatibility during the transition.
"""

from __future__ import annotations

from src.models.concept_tree import ConceptGraph, ConceptNode, build_math_concept_tree


if __name__ == "__main__":
    tree: ConceptGraph = build_math_concept_tree()
    print("Mathematics Concept Graph:")
    print(f"Concept count: {len(tree.nodes)}")

    topic = "derivatives"
    matches = tree.find_by_name(topic)
    if matches:
        node: ConceptNode = matches[0]
        path = tree.learning_path_to(node.concept_id)
        print(f"\nLearning path to '{topic}':")
        for cid in path:
            n = tree.nodes[cid]
            print(f"- {n.domain}: {n.name} ({cid})")
    else:
        print(f"\nTopic '{topic}' not found.")