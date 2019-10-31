class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node


"""
Given two singly linked lists there may be list nodes that are common to both.
(This may not be a bug—it may be desirable from the perspective of reducing
memory footprint, as in the flyweight pattern, or maintaining a canonical form.)
For example, the lists in Figure 7.6 on the following page overlap at Node I.

Write a program that takes two cycle-free singly linked lists, and determines if
there exists a node that is common to both lists.

Hint: Solve the simple cases first.

NOTES:
- The lists overlap if and only if both have the same tail node: once the lists
converge at a node, they cannot diverge at a later node. Therefore, checking for
overlap amounts to finding the tail nodes for each list.

"""

def overlapping_no_cycle_lists(L1, L2):
    """
    Space complexity: O(1)
    Time complexity: O(n)

    """

    def length(L):
        length = 0
        while L:
            length += 1
            L = L.next
        return length

    L1_len, L2_len = length(L1), length(L2)
    if L1_len > L2_len:
        L1, L2 = L2, L1
    for _ in range(abs(L1_len - L2_len)):
        L2 = L2.next

    while L1 and L2 and L1 is not L2:
        L1, L2 = L1.next, L2.next
    return L1
