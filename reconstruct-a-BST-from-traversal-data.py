class BSTNode:
    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right


"""
As discussed in Problem 9.12 on Page 125 there are many different binary trees
that yield the same sequence of visited nodes in an inorder traversal. This is
also true for preorder and postorder traversals. Given the sequence of nodes
that an inorder traversal sequence visits and either of the other two traversal
sequences, there exists a unique binary tree that yields those sequences. Here
we study if it is possible to reconstruct the tree with less traversal
information when the tree is known to be a BST.

It is critical that the elements stored in the tree be unique. If the root
contains key v and the tree contains more occurrences  of v, we cannot always
identify from the sequence whether the subsequent vs are in the left subtree or
the right subtree. For example, for the tree rooted at G in Figure 14.2 on Page
202 the preorder traversal sequence is 285,243,285,401. The same preorder
traversal sequence is seen if 285 appears in the left subtree as the right child
of the node with key 243 and 401 is at the root's right child.

Suppose you are given the sequence in which keys are visited in an inorder
traversal of a BST, and all keys are distinct. Can you reconstruct the BST from
the sequence? If so, write a program to do so. Solve the same problem for
preorder and postorder traversal sequences.

Hint: Draw the five BSTs on the keys 1,2,3, and the corresponding traversal
orders.

NOTES:
- A better approach is to reconstruct the left subtree in the same iteration as
identifying the nodes which lie in it.

"""

def rebuild_bst_from_preorder(preorder_sequence):
    if not preorder_sequence:
        return None

    transition_point = next(
        (i for i, a in enumerate(preorder_sequence) \
            if a > preorder_sequence[0]),
        len(preorder_sequence)
    )

    return BSTNode(
        preorder_sequence[0],
        rebuild_bst_from_preorder(preorder_sequence[1:transition_point]),
        rebuild_bst_from_preorder(preorder_sequence[transition_point:])
    )


def rebuild_bst_from_preorder(preorder_sequence):
    def rebuild_bst_from_preorder_on_value_range(lower_bound, upper_bound):
        if root_idx[0] == len(preorder_sequence):
            return None

        root = preorder_sequence[root_idx[0]]
        if not lower_bound <= root <= upper_bound:
            return None
        root_idx[0] += 1
        left_subtree = rebuild_bst_from_preorder_on_value_range(
            lower_bound,
            root
        )
        right_subtree = rebuild_bst_from_preorder_on_value_range(
            root,
            upper_bound
        )
        return BSTNode(root, left_subtree, right_subtree)

    root_idx = [0]
    return rebuild_bst_from_preorder_on_value_range(float('-inf'), float('inf'))
