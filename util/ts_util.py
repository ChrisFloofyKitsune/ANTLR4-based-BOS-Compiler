""" Utility functions for working with tree-sitter. """

from tree_sitter import Node


def nearest_previous(node: Node, node_type: str) -> Node | None:
    """
    Return the nearest previous sibling or ancestor of the given node that is of the given type.
    """

    current_node = node
    while current_node is not None:
        current_node = current_node.prev_sibling or current_node.parent
        if current_node and current_node.type == node_type:
            return current_node

    return None
