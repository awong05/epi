class BSTNode:
    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right


"""
Write a program that takes as input a binary tree and checks if the tree
satisfies the BST property.

Hint: Is it correct to check for each node that its key is greater than or equal
to the key at its left child and less than or equal to the key at its right
child?

"""

from collections import deque, namedtuple


def is_binary_tree_bst(tree, low_range=float('-inf'), high_range=float('inf')):
    """
    Space complexity: O(h)
    Time complexity: O(n)

    """

    if not tree:
        return True
    elif not low_range <= tree.data <= high_range:
        return False
    return (
        is_binary_tree_bst(tree.left, low_range, tree.data) and \
        is_binary_tree_bst(tree.right, tree.data, high_range)
    )


def is_binary_tree_bst(tree):
    QueueEntry = namedtuple('QueueEntry', ('node', 'lower', 'upper'))

    bfs_queue = deque([QueueEntry(tree, float('-inf'), float('inf'))])

    while bfs_queue:
        front = bfs_queue.popleft()
        if front.node:
            if not front.lower <= front.node.data <= front.upper:
                return False
            bfs_queue += [
                QueueEntry(front.node.left, front.lower, front.node.data),
                QueueEntry(front.node.right, front.node.data, front.upper)
            ]
    return True
