"""
You want to compute the running median of a sequence of numbers. The sequence is
presented to you in a streaming fashion—you cannot back up to read an earlier
value, and you need to output the median after reading in each new element. For,
example, if the input is 1,0,3,5,2,0,1 the output is 1,0.5,1,2,2,1.5,1.

Design an algorithm for computing the running median of a sequence.

Hint: Avoid looking at all values each time you read a new value.

"""

from heapq import heappop, heappush, heappushpop


def online_median(sequence):
    """
    Space complexity: O(n)
    Time complexity: O(nlogn)

    """

    min_heap = []
    max_heap = []
    result = []

    for x in sequence:
        heappush(max_heap, -heappushpop(min_heap, x))
        if len(max_heap) > len(min_heap):
            heappush(min_heap, -heappop(max_heap))

        result.append(0.5 * (min_heap[0] + (-max_heap[0])) if len(min_heap) == len(max_heap else min_heap[0])
    return result
