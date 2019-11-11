"""
This problem is concerned with computing regions within a 2D grid that are
enclosed. See Figure 18.7 for an illustration of the problem.

The computational problem can be formalized using 2D arrays of Bs (blacks) and
Ws (whites). Figure 18.7(a) is encoded by

[B B B B]
[W B W B]
[B W W B]
[B B B B]

Figure 18.7(b) is encoded by

[B B B B]
[W B B B]
[B B B B]
[B B B B]

Let A be a 2D array whose entries are either W or B. Write a program that takes
A, and replaces all Ws that cannot reach a boundary with a B.

Hint: It is easier to compute the complement of the desired result.

NOTES:
- It is easier to focus on the inverse problem, namely identifying Ws that can
reach the boundary.

"""

from collections import deque


def fill_surrounded_regions(board):
    """
    Space complexity: O(mn)
    Time complexity: O(mn)

    """

    n, m = len(board), len(board[0])
    q = deque(
        [(i, j) for k in range(n) for i, j in ((k, 0), (k, m - 1))] + \
        [(i, j) for k in range(m) for i, j in ((0, k), (n - 1, k))]
    )
    while q:
        x, y = q.popleft()
        if 0 <= x < n and 0 <= y < m and board[x][y] == 'W':
            board[x][y] = 'T'
            q.extend([(x - 1, y), (x + 1, y),  (x, y - 1), (x, y + 1)])
    board[:] = [['B' if c != 'T' else 'W' for c in row] for row in board]
