class BSTNode:
    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right


"""
A BST is a sorted data structure, which suggests that it should be possible to
find the k largest keys easily.

Write a program that takes as input a BST and an integer k, and returns the k
largest elements in the BST in decreasing order. For example, if the input is
the BST in Figure 14.1 on Page 198 and k = 3, your program should return
<53,47,43>.

Hint: What does an inorder traversal yield?

NOTES:
- A better approach is to begin with the desired  nodes, and work backwards.
- This amounts to a reverse-inorder traversal.

"""

def find_k_largest_in_bst(tree, k):
    """
    Space complexity: O(1)
    Time complexity: O(h + k)

    """

    def find_k_largest_in_bst_helper(tree):
        if tree and len(k_largest_elements) < k:
            find_k_largest_in_bst_helper(tree.right)
            if len(k_largest_elements) < k:
                k_largest_elements.append(tree.data)
                find_k_largest_in_bst_helper(tree.left)

    k_largest_elements = []
    find_k_largest_in_bst_helper(tree)
    return k_largest_elements
