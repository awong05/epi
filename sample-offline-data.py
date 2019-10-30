"""
This problem is motivated by the need for a company to select a random subset of
its customers to roll out a new feature to. For example, a social networking
company may want to see the effect of a new UI on page visit duration without
taking the chance of alienating all of its users if the rollout is unsuccessful.

Implement an algorithm that takes as input an array of distinct elements and a
size, and returns a subset of the given size of the array elements. All subsets
should be equally likely. Return the result in input array itself.

Hint: How would you construct a random subset of size k + 1 given a random
subset of size k?

NOTES:
- The key to efficiently building a random subset of size exactly k is to first
build one of size k - 1 and then adding one more element, selected randomly from
the rest.

"""

from random import randint


def random_sampling(k, A):
    """
    Space complexity: O(1)
    Time complexity: O(k)

    """

    for i in range(k):
        r = randint(i, len(A) - 1)
        A[i], A[r] = A[r], A[i]
