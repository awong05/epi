"""
Binary search commonly asks for the index of any element of a sorted array that
is equal to a specified element. The following problem has a slight twist on
this.

Write a method that takes a sorted array and a key and returns the index of the
first occurrence of that key in the array. Return -1 if the key does not appear
in the array. For example, when applied to the array in Figure 11.1, your
algorithm should return 3 if the given key is 108; if it is 285, your algorithm
should return 6.

Hint: What happens when every entry equals k? Don't step when you first see k.

"""

def search_first_of_k(A, k):
    """
    Space complexity: O(1)
    Time complexity: O(logn)

    """

    left, right, result = 0, len(A) - 1, -1
    while left <= right:
        mid = (left + right) // 2
        if A[mid] > k:
            right = mid - 1
        elif A[mid] == k:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result
