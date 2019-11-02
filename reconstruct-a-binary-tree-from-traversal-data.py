class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


"""
Many different binary trees yield the same sequence of keys in an inorder,
preorder, or postorder traversal. However, given an inorder traversal and one of
any two other traversal orders of a binary tree, there exists a unique binary
tree that yields those orders, assuming each node holds a distinct key. For
example, the unique binary tree whose inorder traversal sequence is
<F,B,A,E,H,C,D,I,G> and whose preorder traversal sequence is <H,B,F,E,A,C,D,G,I>
is given in Figure 9.5.

Given an inorder traversal sequence and a preorder traversal sequence of a
binary tree write a program to reconstruct the tree. Assume each node has a
unique key.

Hint: Focus on the root.

NOTES:
- The next insight is that we can use the left subtree inorder sequence to
compute the preorder sequence for the left subtree from the preorder sequence
for the entire tree.
- We know the number k of nodes in the left subtree from the location of the
root in the inorder traversal sequence.
- Therefore, the subsequence of k nodes after the root in the preorder traversal
sequence is the preorder traversal sequence for the left subtree.

"""

def binary_tree_from_preorder_inorder(preorder, inorder):
    """
    Space complexity: O(n)
    Time complexity: O(n)

    """

    node_to_inorder_idx = {data: i for i, data in enumerate(inorder)}

    def binary_tree_from_preorder_inorder_helper(
        preorder_start,
        preorder_end,
        inorder_start,
        inorder_end
    ):
        if preorder_end <= preorder_start or inorder_end <= inorder_start:
            return None

        root_inorder_idx = node_to_inorder_idx[preorder[preorder_start]]
        left_subtree_size = root_inorder_idx - inorder_start
        return BinaryTreeNode(
            preorder[preorder_start],
            binary_tree_from_preorder_inorder_helper(
                preorder_start + 1,
                preorder_start + 1 + left_subtree_size,
                inorder_start,
                root_inorder_idx
            ),
            binary_tree_from_preorder_inorder_helper(
                preorder_start + 1 + left_subtree_size,
                preorder_end,
                root_inorder_idx + 1,
                inorder_end
            )
        )

    return binary_tree_from_preorder_inorder_helper(
        0,
        len(preorder),
        0,
        len(inorder)
    )
