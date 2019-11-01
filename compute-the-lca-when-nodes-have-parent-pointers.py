class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


"""
Given two nodes in a binary tree, design an algorithm that computes their LCA.
Assume that each node has a parent pointer.

Hint: The problem is easy if both nodes are the same distance from the root.

"""

def lca(node_0, node_1):
    """
    Space complexity: O(1)
    Time complexity: O(h)

    """

    def get_depth(node):
        depth = 0
        while node:
            depth += 1
            node = node.parent
        return depth

    depth_0, depth_1 = get_depth(node_0), get_depth(node_1)
    if depth_1 > depth_0:
        node_0, node_1 = node_1, node_0

    depth_diff = abs(depth_0 - depth_1)
    while depth_diff:
        node_0 = node_0.parent
        depth_diff -= 1

    while node_0 is not node_1:
        node_0, node_1 = node_0.parent, node_1.parent
    return node_0
