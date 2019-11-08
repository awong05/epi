class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node


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


"""
Implement a routine which sorts lists efficiently. It should be a stable sort,
i.e., the relative positions of equal elements must remain unchanged.

Hint: In what respects are lists superior to arrays?

NOTES:
- We decompose the list into two equal-sized sublists around the node in the
middle of the list.
- We find this node by advancing two iterators through the list, one twice as
fast as the other.
- We recurse on the sublists, and use Solution 7.1 on Page 84 (merge two sorted
lists) to combine the sorted sublists.

"""

def stable_sort_list(L):
    """
    Space complexity: O(logn)
    Time complexity: O(nlogn)

    """

    if not L or not L.next:
        return L
    pre_slow, slow, fast = None, L, L
    while fast and fast.next:
        pre_slow = slow
        fast, slow = fast.next.next, slow.next
    pre_slow.next = None
    return merge_two_sorted_lists(stable_sort_list(L), stable_sort_list(slow))
