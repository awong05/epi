class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node


"""
Although a linked list is supposed to be a sequence of nodes ending in null, it
is possible to create a cycle in a linked list by making the next field of an
element reference to one of the earlier nodes.

Write a program that takes the head of a singly linked list and returns null if
there does not exist a cycle, and the node at the start of the cycle, if a cycle
is present. (You do not know the length of the list in advance.)

Hint: Consider using two iterators, one fast and one slow.

"""

def has_cycle(head):
    """
    Space complexity: O(1)
    Time complexity: O(n)

    """

    def cycle_len(end):
        start, step = end, 0
        while True:
            step += 1
            start = start.next
            if start is end:
                return step

    fast = slow = head
    while fast and fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            cycle_len_advanced_iter = head
            for _ in range(cycle_len(slow)):
                cycle_len_advanced_iter = cycle_len_advanced_iter.next

            it = head
            while it is not cycle_len_advanced_iter:
                it = it.next
                cycle_len_advanced_iter = cycle_len_advanced_iter.next
            return it
    return None
