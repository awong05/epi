"""
An array is said to be cyclically sorted if it is possible to cyclically shift
its entries so that it becomes sorted. For example, the array in Figure 11.2 is
cyclically sorted—a cyclic left shift by 4 leads to a sorted array.

Design an O(logn) algorithm for finding the position of the smallest element in
a cyclically sorted array. Assume all elements are distinct. For example, for
the array in Figure 11.2, your algorithm should return 4.

Hint: Use the divide and conquer principle.

NOTES:
- Note that this problem cannot, in general, be solved in less than linear time
when elements may be repeated.

"""

def search_smallest(A):
    """
    Space complexity: O(1)
    Time complexity: O(logn)

    """

    left, right = 0, len(A) - 1
    while left < right:
        mid = (left + right) // 2
        if A[mid] > A[right]:
            left = mid + 1
        else:
            right = mid
    return left
