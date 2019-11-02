"""
Often data is almost-sorted—for example, a server receives timestamped stock
quotes may arrive slightly after later quotes because of differences in server
loads and network routes. In this problem we address efficient ways to sort such
data.

Write a program which takes as input a very long sequence of numbers and prints
the numbers in sorted order. Each number is at most k away from its correctly
sorted position. (Such an array is sometimes referred to as being k-sorted.) For
example, no number in the sequence <3,-1,2,6,4,5,8> is more than 2 away from its
final sorted position.

Hint: How many numbers must you read after reading the ith number to be sure you
can place it in the correct location?

NOTES:
- Specifically, after we have read k + 1 numbers, the smallest number in that
group must be smaller than all following numbers.

"""

from heapq import heappop, heappush, heappushpop
from itertools import islice


def sort_approximately_sorted_array(sequence, k):
    """
    Space complexity: O(k)
    Time complexity: O(nlogk)

    """

    result = []
    min_heap = []
    for x in islice(sequence, k):
        heappush(min_heap, x)

    for x in sequence:
        smallest = heappushpop(min_heap, x)
        result.append(smallest)

    while min_heap:
        smallest = heappop(min_heap)
        result.append(smallest)

    return result
