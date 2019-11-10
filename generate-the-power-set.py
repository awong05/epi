"""
The power set of a set S is the set of all subsets of S, including both the
empty set 0 and S itself. The power set of {0,1,2} is graphically illustrated in
Figure 15.5.

Write a function that takes as input a set and returns its power set.

Hint: There are 2**n subsets for a given set S of size n. There are 2**k k-bit
words.

NOTES:
- Each subset set must appear in U or in V, so the final result is just U union
V.
- For a given ordering of the elements of S, there exists a one-to-one
correspondence between the 2**n bit arrays of length n and the set of all
subsets of S—the 1s in the n-length bit array v indicate the elements of S in
the subset corresponding to v.
- In particular, when n is less than or equal to the width of an integer on the
architecture (or language) we are working on, we can enumerate bit arrays by
enumerating integers in [0, 2**n - 1] and examining the indices of bits set in
these integers.

"""

from math import log2


def generate_power_set(input_set):
    """
    Space complexity: O(n2**n)
    Time complexity: O(n2**n)

    """

    def directed_power_set(to_be_selected, selected_so_far):
        if to_be_selected == len(input_set):
            power_set.append(list(selected_so_far))
            return

        directed_power_set(to_be_selected + 1, selected_so_far)
        directed_power_set(
            to_be_selected + 1,
            selected_so_far + [input_set[to_be_selected]]
        )

    power_set = []
    directed_power_set(0, [])
    return power_set


def generate_power_set(S):
    """
    Space complexity: O(n2**n)
    Time complexity: O(n2**n)

    """

    power_set = []
    for int_for_subset in range(1 << len(S)):
        bit_array = int_for_subset
        subset = []
        while bit_array:
            subset.append(int(log2(bit_array & ~(bit_array - 1))))
            bit_array &= bit_array - 1
        power_set.append(subset)
    return power_set
