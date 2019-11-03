"""
Many algorithms require as a subroutine the computation of the kth largest
element of an array. The first largest element is simply the largest element.
The nth largest element is the smallest element, where n is the length of the
array.

For example, if the input array A = <3,2,1,5,4>, then A[3] is the first largest
element in A, A[0] is the third largest element in A, and A[2] is the fifth
largest element in A.

Design an algorithm for computing the kth largest element in an array.

Hint: Use divide and conquer in conjunction with randomization.

NOTES:
- Conceptually, to focus on the kth largest element in-place without completely
sorting the array we can select an element at random (the "pivot"), and
partition the remaining entries into those greater than the pivot and those less
than the pivot.
- If there are more than k - 1 elements greater that the pivot, we can discard
elements less than or equal to the pivot—the k-largest element must be greater
than the pivot.
- If there are less than k - 1 elements greater than the pivot, we can discard
elements greater than or equal to the pivot.

"""
from operator import gt
from random import randint


def find_kth_largest(k, A):
    """
    Space complexity: O(1)
    Time complexity: O(n)

    """

    def find_kth(comp):
        def partition_around_pivot(left, right, pivot_idx):
            pivot_value = A[pivot_idx]
            new_pivot_idx = left
            A[pivot_idx], A[right] = A[right], A[pivot_idx]
            for i in range(left, right):
                if comp(A[i], pivot_value):
                    A[i], A[new_pivot_idx] = A[new_pivot_idx], A[i]
                    new_pivot_idx += 1
            A[right], A[new_pivot_idx] = A[new_pivot_idx], A[right]
            return new_pivot_idx

        left, right = 0, len(A) - 1
        while left <= right:
            pivot_idx = randint(left, right)
            new_pivot_idx = partition_around_pivot(left, right, pivot_idx)
            if new_pivot_idx == k - 1:
                return A[new_pivot_idx]
            elif new_pivot_idx > k - 1:
                right = new_pivot_idx - 1
            else:
                left = new_pivot_idx

    return find_kth(gt)
