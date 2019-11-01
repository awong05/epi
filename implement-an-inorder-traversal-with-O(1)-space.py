class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


"""
The direct implementation of an inorder traversal using recursion has O(h) space
complexity, where h is the height of the tree. Recursion can be removed with an
explicit stack, but the space complexity remains O(h).

Write a nonrecursive program for computing the inorder traversal sequence for a
binary tree. Assume nodes have parent fields.

Hint: How can you tell whether a node is a left child or right child of its
parent?

NOTES:
- What we do after that depends on whether the subtree we returned from was the
left subtree or right subtree of the parent.
- In the former,  we visit the parent, and then its right subtree; in the
latter, we return from the parent itself.

"""

def inorder_traversal(tree):
    """
    Space complexity: O(1)
    Time complexity: O(n)

    """

    prev, result = None, []
    while tree:
        if prev is tree.parent:
            if tree.left:
                next = tree.left
            else:
                result.append(tree.data)
                next = tree.right or tree.parent
        elif tree.left is prev:
            result.append(tree.data)
            next = tree.right or tree.parent
        else:
            next = tree.parent
        prev, tree = tree, next
    return result
