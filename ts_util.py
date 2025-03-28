""" Utility functions for working with tree-sitter. """

from tree_sitter import Node


def nearest_previous(node: Node, node_type: str) -> Node | None:
    """
    Return the nearest previous sibling or ancestor of the given node that is of the given type.
    """

    # go to the top...
    top_node = node
    while top_node.parent is not None:
        top_node = top_node.parent

    # ...so we can walk right back down...
    cursor = top_node.walk()
    while cursor.node != node:
        cursor.goto_first_child_for_byte(node.start_byte)

    # ...to find what we're looking for.
    # (feels like there should be a better way to do this?)
    while cursor.goto_previous_sibling() or cursor.goto_parent():
        if cursor.node.type == node_type:
            return cursor.node

    return None
