class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node


"""
Without knowing the length of a linked list, it is not trivial to delete the kth
last element in a singly linked list.

Given a singly linked list and an integer k, write a program to remove the kth
last element from the list. Your algorithm cannot use more than a few words of
storage, regardless of the length of the list. In particular, you cannot assume
that it is possible to record the length of the list.

Hint: If you know the length of the list, can you find the kth last node using
two iterators?

"""

def remove_kth_last(L, k):
    """
    Space complexity: O(1)
    Time complexity: O(n)

    """

    dummy_head = ListNode(0, L)
    first = dummy_head.next
    for _ in range(k):
        first = first.next

    second = dummy_head
    while first:
        first, second = first.next, second.next
    second.next = second.next.next
    return dummy_head.next
