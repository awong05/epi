"""
Binary trees are formally defined in Chapter 9. In particulaar, each node in a
binary tree has a depth, which is its distance from the root.

Given a binary tree, return an array consisting of the keys at the same level.
Keys should appear in the order of the corresponding nodes' depths, breaking
ties from left to right. For example, you should return
<<314>,<6,6>,<271,561,2,271>,<28,0,3,1,28>,<17,401,257>,<641>> for the binary
tree in Figure 9.1 on Page 112.

Hint: First think about solving this problem with a pair of queues.

"""

def binary_tree_depth_order(tree):
    """
    Space complexity: O(m)
    Time complexity: O(n)

    """

    result = []
    if not tree:
        return result

    curr_depth_nodes = [tree]
    while curr_depth_nodes:
        result.append([curr.data for curr in curr_depth_nodes])
        curr_depth_nodes = [
            child
            for curr in curr_depth_nodes for child in (curr.left, curr.right)
            if child
        ]
    return result
