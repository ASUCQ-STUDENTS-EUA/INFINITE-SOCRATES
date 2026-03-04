"""
Concept Tree for Basic Mathematics
Represents hierarchical relationships between math topics.
Useful for guiding students through prerequisite chains.
"""

class ConceptNode:
    """A node in the concept tree representing a math topic."""
    
    def __init__(self, name, description=""):
        self.name = name
        self.description = description
        self.children = []  # list of ConceptNode objects
        self.parent = None

    def add_child(self, child_node):
        """Add a child topic to this node."""
        child_node.parent = self
        self.children.append(child_node)

    def get_depth(self):
        """Return the depth of this node from the root."""
        depth = 0
        node = self
        while node.parent:
            depth += 1
            node = node.parent
        return depth

    def display(self, level=0):
        """Print the tree rooted at this node."""
        indent = "  " * level
        print(f"{indent}- {self.name}")
        for child in self.children:
            child.display(level + 1)

    def find_topic(self, topic_name):
        """Search for a topic by name in this subtree."""
        if self.name.lower() == topic_name.lower():
            return self
        for child in self.children:
            result = child.find_topic(topic_name)
            if result:
                return result
        return None


def build_math_concept_tree():
    """Construct a sample concept tree for basic mathematics."""
    
    # Root node
    math = ConceptNode("Mathematics", "The study of numbers, quantities, and shapes.")
    
    # Level 1: Major branches
    arithmetic = ConceptNode("Arithmetic", "Basic operations with numbers.")
    algebra = ConceptNode("Algebra", "Symbols and rules for manipulating equations.")
    geometry = ConceptNode("Geometry", "Properties of space and figures.")
    calculus = ConceptNode("Calculus", "Change and motion; derivatives and integrals.")
    
    math.add_child(arithmetic)
    math.add_child(algebra)
    math.add_child(geometry)
    math.add_child(calculus)
    
    # Arithmetic subtopics
    arithmetic.add_child(ConceptNode("Addition", "Combining numbers."))
    arithmetic.add_child(ConceptNode("Subtraction", "Taking away numbers."))
    arithmetic.add_child(ConceptNode("Multiplication", "Repeated addition."))
    arithmetic.add_child(ConceptNode("Division", "Splitting into equal parts."))
    
    # Algebra subtopics
    algebra.add_child(ConceptNode("Linear Equations", "Equations of the form ax + b = 0."))
    algebra.add_child(ConceptNode("Quadratic Equations", "Equations of the form ax² + bx + c = 0."))
    algebra.add_child(ConceptNode("Polynomials", "Expressions with multiple terms."))
    algebra.add_child(ConceptNode("Functions", "Relations between inputs and outputs."))
    
    # Geometry subtopics
    geometry.add_child(ConceptNode("Points and Lines", "Basic elements."))
    geometry.add_child(ConceptNode("Angles", "Measurement of turn."))
    geometry.add_child(ConceptNode("Triangles", "Three-sided polygons."))
    geometry.add_child(ConceptNode("Circles", "Set of points equidistant from center."))
    
    # Calculus subtopics
    calculus.add_child(ConceptNode("Limits", "Approaching a value."))
    calculus.add_child(ConceptNode("Derivatives", "Rate of change."))
    calculus.add_child(ConceptNode("Integrals", "Area under a curve."))
    calculus.add_child(ConceptNode("Series", "Sum of sequences."))
    
    return math


if __name__ == "__main__":
    # Build and display the concept tree
    tree = build_math_concept_tree()
    print("Mathematics Concept Tree:")
    tree.display()
    
    # Example: Find a topic
    topic = "derivatives"
    node = tree.find_topic(topic)
    if node:
        print(f"\nFound topic '{topic}' at depth {node.get_depth()}")
        if node.parent:
            print(f"Parent: {node.parent.name}")
    else:
        print(f"\nTopic '{topic}' not found.")