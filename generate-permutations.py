"""
This problem is concerned with computing all permutations of an array. For
example, if the array is <2,3,5,7> one output could be <2,3,5,7>, <2,3,7,5>,
<2,5,3,7>, <2,5,7,3>, <2,7,3,5>, <2,7,5,3>, <3,2,5,7>, <3,2,7,5>, <3,5,2,7>,
<3,5,7,2>, <3,7,2,5>, <3,7,5,2>, <5,2,3,7>, <5,2,7,3>, <5,3,2,7>, <5,3,7,2>,
<5,7,2,3>, <5,7,2,3>, <7,2,3,5>, <7,2,5,3>, <7,3,2,5>, <7,3,5,2>, <7,5,2,3>,
<7,5,3,2>. (Any other ordering is acceptable too.)

Write a program which takes as input an array of distinct integers and generates
all permutations of that array. No permutation of the array may appear more than
once.

Hint: How many possible values are there for the first element?

NOTES:
- The idea is to generate all permutations that begin with A[0], then all
permutations that begin with A[1], and so on.
- Computing all permutations beginning with A[0] entails computing all
permutations of A[1,n - 1], which suggests the use of recursion.
- To compute all permutations beginning with A[1] we swap A[0] with A[1] and
compute all permutations of the updated A[1,n - 1].

"""

def permutations(A):
    """
    Time complexity: O(n*n!)

    """

    def directed_permutations(i):
        if i == len(A) - 1:
            result.append(A.copy())
            return

        for j in range(i, len(A)):
            A[i], A[j] = A[j], A[i]
            directed_permutations(i + 1)
            A[i], A[j] = A[j], A[i]

    result = []
    directed_permutations(0)
    return result


def permutations(A):
    """
    Time complexity: O(n*n!)

    """

    result = []
    while True:
        result.append(A.copy())
        A = next_permutation(A)
        if not A:
            break
    return result
