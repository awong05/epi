"""
Write a progam which takes as input an array of digits encoding a nonnegative
decimal integer D and updates the array to represent the integer D + 1. For
example, if the input is <1,2,9> then you should update the array to <1,3,0>.
Your algorithm should work even if it is implemented in a language that has
finite-prevision arithmetic.

Hint: Experiment with concrete examples.

NOTES:
- There is a carry-out, so we need one more digit to store the result. A slick
way to do this is to append a 0 at the end of the array, and update the first
entry to 1. [L31]

"""

def plus_one(A):
    """
    Space complexity: O(1)
    Time complexity: O(n)

    """

    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i - 1] += 1
    if A[0] == 10:
        A[0] = 1
        A.append(0)
    return A
