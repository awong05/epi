class BSTNode:
    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right

    def __repr__(self):
        return str(self.data)


"""
Write a program that takes aas input a BST and a value, and returns the first
key that would appear in an inorder traversal which is greater than the input
value. For example, when applied to the BST in Figure 14.1 on Page 198 you
should return 29 for input 23.

Hint: Perform binary search, keeping some additional state.

NOTES:
- We store the best candidate for the result and update that candidate as we
iteratively descend the tree, eliminating subtrees by comparing the keys stored
at nodes with the input value.

"""

def find_first_greater_than_k(tree, k):
    """
    Space complexity: O(1)
    Time complexity: O(h)

    """

    subtree, first_so_far = tree, None
    while subtree:
        if subtree.data > k:
            first_so_far, subtree = subtree, subtree.left
        else:
            subtree = subtree.right
    return first_so_far
