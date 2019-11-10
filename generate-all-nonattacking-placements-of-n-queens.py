"""
A nonattacking placement of queens is one in which no two queens are in the same
row, column, or diagonal. See Figure 15.4 for an example.

Write a program which returns all distinct nonattacking placements of n queens
on an n x n chessboard, where n is an input to the program.

Hint: If the first queen is placed at (i, j), where can the remaining queens
definitely not be placed?

NOTES:
- It can be represented by an array of length n, where the ith entry is the
location of the queen on Row i.

"""

def n_queens(n):
    def solve_n_queens(row):
        if row == n:
            result.append(list(col_placement))
            return
        for col in range(n):
            if all(
                abs(c - col) not in (0, row - i) \
                for i, c in enumerate(col_placement[:row])
            ):
                col_placement[row] = col
                solve_n_queens(row + 1)

    result, col_placement = [], [0] * n
    solve_n_queens(0)
    return result
