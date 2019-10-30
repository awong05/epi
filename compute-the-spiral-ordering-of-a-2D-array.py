"""
A 2D array can be written as a sequence in several orders—the most natural ones
being row-by-row or column-by-column. In this problem we explore the problem of
writing the 2D array in spiral order. For example, the spiral ordering for the
2D array in Figure 5.3(a) on the following page is <1,2,3,6,9,8,7,4,5>. For
Figure 5.3(b) on the next page, the spiral ordering is
<1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10>.

Write a program which takes an n x n 2D array and returns the spiral ordering of
the array.

Hint: Use case analysis and divide-and-conquer.

"""

def matrix_in_spiral_order(square_matrix):
    """
    Space complexity: O(1)
    Time complexity: O(n**2)

    """

    def matrix_layer_in_clockwise(offset):
        if offset == len(square_matrix) - offset - 1:
            spiral_ordering.append(square_matrix[offset][offset])
            return
        spiral_ordering.extend(square_matrix[offset][offset:-1 - offset])
        spiral_ordering.extend(
            list(zip(*square_matrix))[-1 - offset][offset:-1 - offset]
        )
        spiral_ordering.extend(
            square_matrix[-1 - offset][-1 - offset:offset:-1]
        )
        spiral_ordering.extend(
            list(zip(*square_matrix))[offset][-1 - offset:offset:-1]
        )

    spiral_ordering = []
    for offset in range((len(square_matrix) + 1) // 2):
        matrix_layer_in_clockwise(offset)
    return spiral_ordering

def matrix_in_spiral_order(square_matrix):
    """
    Space complexity: O(1)
    Time complexity: O(n**2)

    """

    SHIFT = ((0, 1), (1, 0), (0, -1), (-1, 0))
    direction = x = y = 0
    spiral_ordering = []

    for _ in range(len(square_matrix)**2):
        spiral_ordering.append(square_matrix[x][y])
        square_matrix[x][y] = 0
        next_x, next_y = x + SHIFT[direction][0], y + SHIFT[direction][1]
        if (next_x not in range(len(square_matrix)) or \
            next_y not in range(len(square_matrix)) or \
            square_matrix[next_x][next_y] == 0
        ):
            direction = (direction + 1) & 3
            next_x, next_y = x + SHIFT[direction][0], y + SHIFT[direction][1]
        x, y = next_x, next_y
    return spiral_ordering
