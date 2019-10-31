class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node


"""
Consider a singly linked list whose nodes are numbered starting at 0. Define the
even-odd merge of the list consisting of the even-numbered nodes followed by the
odd-numbered nodes. The even-odd merge is illustrated in Figure 7.10.

Write a program that computes the even-odd merge.

Hint: Use temporary additional storage.

"""

def even_odd_merge(L):
    """
    Space complexity: O(1)
    Time complexity: O(n)

    """

    if not L:
        return L

    even_dummy_head, odd_dummy_head = ListNode(0), ListNode(0)
    tails, turn = [even_dummy_head, odd_dummy_head], 0
    while L:
        tails[turn].next = L
        L = L.next
        tails[turn] = tails[turn].next
        turn ^= 1
    tails[1].next = None
    tails[0].next = odd_dummy_head.next
    return even_dummy_head.next
