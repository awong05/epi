"""
Sudoku is a popular logic-based combinatorial number placement puzzle. The
objective is to fill a 9 x 9 grid with digits subject to the constraint that
each column, each row, and each of the nine 3 x 3 sub-grids that compose the
grid contains unique integers in [1, 9]. The grid is initialized with a partial
assignment as shown in Figure 5.2(a); a complete solution is shown in
Figure 5.2(b).

Check whether a 9 x 9 2D array representing a partially completed Sudoku is
valid. Specifically, check that no row, column, or 3 x 3 2D subarray contains
duplicates. A 0-value in the 2D array indicates that entry is blank; every other
entry is in [1, 9].

Hint: Directly test the constraints. Use an array to encode sets.

"""

from collections import Counter
from math import sqrt


def is_valid_sudoku(partial_assignment):
    """
    Space complexity: O(n)
    Time complexity: O(n**2)

    """

    def has_duplicate(block):
        block = list(filter(lambda x: x != 0, block))
        return len(block) != len(set(block))

    n = len(partial_assignment)
    if any(
        has_duplicate([partial_assignment[i][j] for j in range(n)]) or \
        has_duplicate([partial_assignment[j][i] for j in range(n)]) \
        for i in range(n)
    ):
        return False

    region_size = int(sqrt(n))
    return all(not has_duplicate([
        partial_assignment[a][b]
        for a in range(region_size * I, region_size * (I + 1))
        for b in range(region_size * J, region_size * (J + 1))
    ]) for I in range(region_size) for J in range(region_size))

def is_valid_sudoku_pythonic(partial_assignment):
    """
    Space complexity: O(n)
    Time complexity: O(n**2)

    """

    region_size = int(sqrt(len(partial_assignment)))
    return max(
        Counter(
            k
            for i, row in enumerate(partial_assignment)
            for j, c in enumerate(row)
            if c != 0
            for k in (
                (i, str(c)),
                (str(c), j),
                (i / region_size, j / region_size, str(c)))
        ).values(),
        default=0
    ) <= 1
