"""
The problem of finding the longest nondecreasing subsequence in a sequence of
integers has implications to many disciplines, including string matching and
analyzing card games. As a concrete instance, the length of a longest
nondecreasing subsequence for the array in Figure 16.15 is 4. There are multiple
longest nondecreasing subsequences, e.g., <0,4,10,14> and <0,2,6,9>. Note that
elements of non-decreasing subsequence are not required to immediately follow
each other in the original sequence.

Write a program that takes as input an array of numbers and returns the length
of a longest nondecreasing subsequence in the array.

Hint: Express the longest nondecreasing subsequence ending at an entry in terms
of the longest nondecreasing subsequence appearing in the subarray consisting of
preceding elements.

"""

def longest_nondecreasing_subsequence_length(A):
    """
    Space complexity: O(n)
    Time complexity: O(n**2)

    """

    max_length = [1] * len(A)
    for i in range(1, len(A)):
        max_length[i] = max(1 + max(
            [max_length[j] for j in range(i)
             if A[i] >= A[j]], default=0), max_length[i])
    return max(max_length)
