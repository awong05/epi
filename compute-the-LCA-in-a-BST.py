class BSTNode:
    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right


"""
Since a BST is a specialized binary tree, the notion of lowest common ancestor,
as expressed in Problem 9.4 on Page 118, holds for BSTs too.

In general, computing the LCA of two nodes in a BST is no easier than computing
the LCA in a binary tree, since structurally a binary tree can be viewed as a
BST where all the keys are equal. However, when the keys are distinct, it is
possible to improve on the LCA algorithms for binary trees.

Design an algorithm that takes as input a BST and two nodes, and returns the LCA
of the two nodes. For example, for the BST in Figure 14.1 on Page 198, and nodes
C and G, your algorithm should return B. Assume all keys are distinct. Nodes do
not have references to their parents.

Hint: Take advantage of the BST property.

"""

def find_LCA(tree, s, b):
    """
    Space complexity: O(1)
    Time complexity: O(h)

    """

    while tree.data < s.data or tree.data > b.data:
        while tree.data < s.data:
            tree = tree.right
        while tree.data > b.data:
            tree = tree.left
    return tree
