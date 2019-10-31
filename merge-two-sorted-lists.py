class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node


"""
Consider two singly linked lists in which each node holds a number. Assume the
lists are sorted, i.e., numbers in the lists appear in ascending order within
each list. The merge of the two lists is a list consisting of the nodes of the
two lists in which numbers appear in ascending order. Merge is illustrated in
Figure 7.3.

Write a program that takes two lists, assumed to be sorted, and returns their
merge. The only field your program can change in a node is its next field.

Hint: Two sorted arrays can be merged using two indices. For lists, take care
when one iterator reaches the end.

"""

def merge_two_sorted_lists(L1, L2):
    """
    Space complexity: O(1)
    Time complexity: O(n + m)

    """

    dummy_head = tail = ListNode()

    while L1 and L2:
        if L1.data < L2.data:
            tail.next, L1 = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next
        tail = tail.next

    tail.next = L1 or L2
    return dummy_head.next
