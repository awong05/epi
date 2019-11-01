class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


"""
A binary tree is said to be height balanced if for each node in the tree, the
difference in the height of its left and right subtrees is at most one. A
perfect binary tree is height-balanced, as is a complete binary tree. A height-
balanced binary tree does not have to be perfect or complete—see Figure 9.2
on the next page for an example.

Write a program that takes as input the root of a binary tree and checks whether
the tree is height-balanced.

Hint: Think of a classic binary tree algorithm.

NOTES:
- We can solve this problem using less storage by observing that we do not need
to store the heights of all nodes at the same time.
- Once we are done with a subtree, all we need to know is whether it is height-
balanced, and if so, what its height is—we do not need any information about
descendents of the subtree's root.

"""

from collections import namedtuple


def is_balanced_binary_tree(tree):
    """
    Space complexity: O(h)
    Time complexity: O(n)

    """

    BalancedStatusWithHeight = namedtuple(
        'BalancedStatusWithHeight',
        ('balanced', 'height')
    )

    def check_balanced(tree):
        if not tree:
            return BalancedStatusWithHeight(True, -1)

        left_result = check_balanced(tree.left)
        if not left_result.balanced:
            return BalancedStatusWithHeight(False, 0)

        right_result = check_balanced(tree.right)
        if not right_result.balanced:
            return BalancedStatusWithHeight(False, 0)

        is_balanced = abs(left_result.height - right_result.height) <= 1
        height = max(left_result.height, right_result.height) + 1
        return BalancedStatusWithHeight(is_balanced, height)

    return check_balanced(tree).balanced
