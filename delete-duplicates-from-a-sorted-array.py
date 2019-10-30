"""
This problem is concerned with deleting repeated elements from a sorted array.
For example, for the array <2,3,5,5,7,11,11,11,13>, then after deletion, the
array is <2,3,5,7,11,13,0,0,0>. After deleting repeated elements, there are 6
valid entries. There are no requirements as to the values stored beyond the
last valid element.

Write a program which takes as input a sorted array and updates it so that all
duplicates have been removed and the remaining elements have been shifted left
to fill the emptied indices. Return the number of valid elements. Many languages
have library functions for performing this operation—you cannot use these
functions.

Hint: There is an O(n) time and O(1) space solution.

"""

def delete_duplicates(A):
    """
    Space complexity: O(1)
    Time complexity: O(n)

    """

    if not A:
        return 0
    write_index = 1
    for i in range(1, len(A)):
        if A[write_index - 1] != A[i]:
            A[write_index] = A[i]
            write_index += 1
    return write_index
