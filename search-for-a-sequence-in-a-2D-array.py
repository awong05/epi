"""
Suppose you are given a 2D array of integers (the "grid"), and a 1D array of
integers (the "pattern"). We say the pattern occurs in the grid if it is
possible to start from some entry in the grid and traverse adjacent entries in
the order specified by the pattern till all entries in the pattern have been
visited. The entries adjacent to an entry are the ones directly above, below, to
the left, and to the right, assuming they exist. For example, the entries
adjacent to (3,4) are (3,3), (3,5), (2,4) and (4,4). It is acceptable to visit
an entry in the grid more than once.

As an example, if the grid is

[1 2 3]
[3 4 5]
[5 6 7]

and the pattern is <1,3,4,6>, then the pattern occurs in the grid—consider the
entries <(0,0),(1,0),(1,1),(2,1)>. However, <1,2,3,4> does not occur in the
grid.

Write a program that takes as arguments a 2D array and a 1D array, and checks
whether the 1D array occurs in the 2D array.

Hint: Start with length 1 prefixes of the 1D array, then move on to length 2,3,
... prefixes.

NOTES:
- In the  program below, we cache intermediate results to avoid repeated calls
to the recursion with identical arguments.

"""

def is_pattern_contained_in_grid(grid, S):
    """
    Space complexity: O(nm|S|)
    Time complexity: O(nm|S|)

    """

    def is_pattern_suffix_contained_starting_at_xy(x, y, offset):
        if len(S) == offset:
            return True

        if (0 <= x < len(grid) and 0 <= y < len(grid[x]) and \
            grid[x][y] == S[offset] and \
            (x, y, offset) not in previous_attempts and \
            any (
                is_pattern_suffix_contained_starting_at_xy(
                    x + a, y + b, offset + 1
                ) for a, b in ((-1, 0), (1, 0), (0, -1), (0, 1))
            )
        ):
            return True
        previous_attempts.add((x, y, offset))
        return False

    previous_attempts = set()
    return any(
        is_pattern_suffix_contained_starting_at_xy(i, j, 0)
        for i in range(len(grid)) for j in range(len(grid[i]))
    )
