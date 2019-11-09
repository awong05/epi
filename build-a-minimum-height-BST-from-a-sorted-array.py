class BSTNode:
    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right


"""
Given a sorted array, the number of BSTs that can be built on the entries in the
array grows enormously with its size. Some of these trees are skewed, and are
closer to lists; others are more balanced. See Figure 14.3 on Page 205 for an
example.

How would you build a BST of minimum possible height from a sorted array?

Hint: Which element should be the root?

"""

def build_min_height_bst_from_sorted_array(A):
    """
    Time complexity: O(n)

    """

    def build_min_height_bst_from_sorted_subarray(start, end):
        if start >= end:
            return None
        mid = (start + end) // 2
        return BSTNode(A[mid],
            build_min_height_bst_from_sorted_subarray(start, mid),
            build_min_height_bst_from_sorted_subarray(mid + 1, end)
        )

    return build_min_height_bst_from_sorted_subarray(0, len(A))
