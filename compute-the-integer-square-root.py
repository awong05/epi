"""
Write a program which takes a nonnegative integer and returns the largest
integer whose square is less than or equal to the given integer. For example, if
the input is 16, return 4; if the input is 300, return 17, since 17**2 = 289 <
300 and 18**2 = 324 > 300.

Hint: Look out for a corner-case.

NOTES:
- The algorithm terminates when the interval is empty, in which case every
number less than l has a square less than or equal to k and l's square is
greater than k, so the result is l - 1.

"""

def square_root(k):
    """
    Space complexity: O(1)
    Time complexity: O(logk)

    """

    left, right = 0, k
    while left <= right:
        mid = (left + right) // 2
        mid_squared = mid * mid
        if mid_squared <= k:
            left = mid + 1
        else:
            right = mid - 1
    return left - 1
