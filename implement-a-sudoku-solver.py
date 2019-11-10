"""
Implement a Sudoku solver. See Problem 5.17 on Page 60 for a definition of
Sudoku.

Hint: Apply the constraints to speed up a brute-force algorithm.

"""

from itertools import product
from math import sqrt


def solve_sudoku(partial_assignment):
    def solve_partial_sudoku(i, j):
        if i == len(partial_assignment):
            i = 0
            j += 1
            if j == len(partial_assignment[i]):
                return True

        if partial_assignment[i][j] != EMPTY_ENTRY:
            return solve_partial_sudoku(i + 1, j)

        def valid_to_add(i, j, val):
            if any(
                val == partial_assignment[k][j] \
                for k in range(len(partial_assignment))
            ):
                return False

            if val in partial_assignment[i]:
                return False

            region_size = int(sqrt(len(partial_assignment)))
            I = i
            J = j
            return not any(
                val == partial_assignment[region_size * I + a][region_size * J + b] \
                for a, b in product(range(region_size), repeat=2)
            )

        for val in range(1, len(partial_assignment) + 1):
            if valid_to_add(i, j, val):
                partial_assignment[i][j] = val
                if solve_partial_sudoku(i + 1, j):
                    return True
        partial_assignment[i][j] = EMPTY_ENTRY
        return False

    EMPTY_ENTRY = 0
    return  solve_partial_sudoku(0, 0)
