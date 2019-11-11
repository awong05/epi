"""
Let A be a Boolean 2D array encoding a black-and-white image. The entry A(a,b)
can be viewed as encoding the color at entry (a,b). Call two entries adjacent if
one is to the left, right, above or below the other. Note that the definition
implies that an entry can be adjacent to at most four other entries, and that
adjacency is symmetric, i.e., if e0 is adjacent to entry e1, then e1 is adjacent
to e0.

Define a path  from entry e0 to entry e1 to be a sequence of adjacent entries,
starting at e0, ending at e1, with successive entries being adjacent. Define the
region associated with a point (i,j) to be all points (i',j') such that there
exists a path from (i,j) to (i',j') in which all entries are the same color. In
particular this implies (i,j) and (i',j')  must be the same color.

Implement a routine that takes an n x m Boolean array A together with an entry
(x,y) and flips the color of the region associated with (x,y). See Figure 18.6
for an example of flipping.

Hint: Solve this conceptually, then think about implementation optimizations.

"""

from collections import deque, namedtuple


def flip_color(x, y, A):
    """
    Space complexity: O(m + n)
    Time complexity: O(mn)

    """

    Coordinate = namedtuple('Coordinate', ('x', 'y'))
    color = A[x][y]
    q = deque([Coordinate(x, y)])
    A[x][y] = 1 - A[x][y]
    while q:
        x, y = q.popleft()
        for d in (0, 1), (0, -1), (1, 0), (-1, 0):
            next_x, next_y = x + d[0], y +  d[1]
            if (0 <= next_x < len(A) and 0 <= next_y < len(A[next_x]) and \
                A[next_x][next_y] == color):
                A[next_x][next_y] = 1 - A[next_x][next_y]
                q.append(Coordinate(next_x, next_y))


def flip_color(x, y, A):
    """
    Time complexity: O(mn)

    """

    color = A[x][y]
    A[x][y] = 1 - A[next_x][next_y]
    for d in (0, 1), (0, -1), (1, 0), (-1, 0):
        next_x, next_y = x + d[0], y +  d[1]
        if (0 <= next_x < len(A) and 0 <= next_y < len(A[next_x]) and \
            A[next_x][next_y] == color):
            flip_color(next_x, next_y, A)
