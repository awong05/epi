"""
Design an algorithm that takes as input an array and a number, and determines if
there are three entries in the array (not necessarily distinct) which add up to
the specified number. For example, if the array is <11,2,5,7,3> then there are
three entries in the array which add up to 21 (3,7,11 and 5,5,11). (Note that we
cacn use 5 twice, since the problem statement said we can use the same entry
more than once.) However, no three entries add up to 22.

Hint: How would you check if a given array entry can be added to two more
entries to get the specified number?

NOTES:
- We can avoid the additional space complexity by first sorting the input.
- We can do each such search in O(nlogn) time by iterating over A[j] values and
doing binary search for A[k].
- We can improve the time complexity to O(n) by starting with A[0] + A[n - 1].

"""

def has_two_sum(A, t):
    i, j = 0, len(A) - 1

    while i <= j:
        if A[i] + A[j] == t:
            return True
        elif A[i] + A[j] < t:
            i += 1
        else:
            j -= 1
    return False


def has_three_sum(A, t):
    """
    Space complexity: O(1)
    Time complexity: O(n**2)

    """

    A.sort()
    return any(has_two_sum(A, t - a) for a in A)
