"""
Legacy entry point for the concept tree.

The canonical implementation now lives at `src/models/concept_tree.py`.
This file stays for backward compatibility during the transition.
"""

from __future__ import annotations

from src.models.concept_tree import ConceptNode, build_math_concept_tree


if __name__ == "__main__":
    tree = build_math_concept_tree()
    print("Mathematics Concept Tree:")
    tree.display()

    topic = "derivatives"
    node: ConceptNode | None = tree.find_topic(topic)
    if node:
        print(f"\nFound topic '{topic}' at depth {node.get_depth()}")
        if node.parent:
            print(f"Parent: {node.parent.name}")
    else:
        print(f"\nTopic '{topic}' not found.")