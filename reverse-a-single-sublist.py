class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node


"""
This problem is concerned with reversing a sublist within a list. See Figure 7.4
for an example of sublist reversal.

Write a program which takes a singly linked list L and two integers s and f as
arguments, and reverses the order of the nodes from the sth node to the fth
node, inclusive. The numbering begins at 1, i.e., the head node is the first
node. Do not allocate additional nodes.

Hint: Focus on the successor fields which have to be updated.

"""

def reverse_sublist(L, start, finish):
    dummy_head = sublist_head = ListNode(0, L)
    for _ in range(1, start):
        sublist_head = sublist_head.next

    sublist_iter = sublist_head.next
    for _ in range(finish - start):
        temp = sublist_iter.next
        sublist_iter.next, temp.next, sublist_head.next = (
            temp.next,
            sublist_head.next
            temp
        )
    return dummy_head.next
