"""
Problem 9.4 on Page 118 is concerned with computing the LCA in a binary tree
with parent pointers in time proportional to the height of the tree. The
algorithm presented in Solution 9.4 on Page 118 entails traversing all the way
up to the root even if the nodes whose LCA is being computed are very close to
their LCA.

Design an algorithm for computing the LCA of two nodes in a binary tree. The
algorithm's time complexity should depend only on the distance from the nodes
to the LCA.

Hint: Focus on the extreme case described in the problem introduction.

NOTES:
- Intuitively, the brute-force approach is suboptimal because it potentially
processes nodes well above the LCA.
- We can avoid this by alternating moving upwards from the two nodes and storing
the nodes visited as we move up in a hash table.

"""

def lca(node_0, node_1):
    """
    Space complexity: O(D0 + D1)
    Time complexity: O(D0 + D1)

    """

    iter_0, iter_1 = node_0, node_1
    nodes_on_path_to_root = set()
    while iter_0 or iter_1:
        if iter_0:
            if iter_0 in nodes_on_path_to_root:
                return iter_0
            nodes_on_path_to_root.add(iter_0)
            iter_0 = iter_0.parent
        if iter_1:
            if iter_1 in nodes_on_path_to_root:
                return iter_1
            nodes_on_path_to_root.add(iter_1)
            iter_1 = iter_1.parent
    raise ValueError('node_0 and node_1 are not in the same tree')
