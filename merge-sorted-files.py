"""
This problem is motivated by the following scenario. You are given 500 files,
each containing stock trade information for an S&P 500 company. Each trade is
encoded by a line in the following format: 1232111,AAPL,30,456.12.

The first number is the time of the trade expressed as the number of
milliseconds since the start of the day's trading. Lines within each file are
sorted in increasing order of time. The remaining values are the stock symbol,
number of shares, and price. You are to create a single file containing all the
trades from the 500 files, sorted in order of increasing trade times. The
individual files are of the order of 5-100 megabytes; the combined file will be
of the order of five gigabytes. In the abstract, we are trying to solve the
following problem.

Write a program that takes as input a set of sorted sequences and computes the
union of these sequences as a sorted sequence. For example, if the input is
<3,5,7>, <0,6>, <0,6,28>, then the output is <0,0,3,5,6,6,7,8>.

Hint: Which part of each sequence is significant as the algorithm executes?

"""

from heapq import heappop, heappush, merge


def merge_sorted_arrays(sorted_arrays):
    """
    Space complexity: O(k)
    Time complexity: O(nlogk)

    """

    min_heap = []
    sorted_arrays_iters = [iter(x) for x in sorted_arrays]

    for i, it in enumerate(sorted_arrays_iters):
        first_element = next(it, None)
        if first_element is not None:
            heappush(min_heap, (first_element, i))

    result = []
    while min_heap:
        smallest_entry, smallest_array_i = heappop(min_heap)
        smallest_array_iter = sorted_arrays_iters[smallest_array_i]
        result.append(smallest_entry)
        next_element = next(smallest_array_iter, None)
        if next_element is not None:
            heappush(min_heap, (next_element, smallest_array_i))
    return result


def merge_sorted_arrays_pythonic(sorted_arrays):
    """
    Space complexity: O(k)
    Time complexity: O(nlogk)

    """

    return list(merge(*sorted_arrays))
