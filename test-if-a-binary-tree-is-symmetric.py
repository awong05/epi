class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


"""
A binary tree is symmetric if you can draw a vertical line through the root and
then the left subtree is the mirror image of the right subtree. The concept of a
symmetric binary tree is illustrated in Figure 9.3.

Write a program that checks whether a binary tree is symmetric.

Hint: The definition of symmetry is recursive.

NOTES:
- All that is important is whether a pair of subtrees are mirror images.

"""

def is_symmetric(tree):
    """
    Space complexity: O(h)
    Time complexity: O(n)

    """

    def check_symmetric(subtree_0, subtree_1):
        if not subtree_0 and not subtree_1:
            return True
        elif subtree_0 and subtree_1:
            return (
                subtree_0.data == subtree_1.data and \
                check_symmetric(subtree_0.left, subtree_1.right) and \
                check_symmetric(subtree_0.right, subtree_1.left)
            )
        return False

    return not tree or check_symmetric(tree.left, tree.right)
