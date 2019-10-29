"""
This problem is concerned with rectangles whose sides are parallel to the X-axis
and Y-axis. See Figure 4.2 for examples.

Write a program which tests if two rectangles have a nonempty intersection. If
the intersection is nonempty, return the rectangle formed by their intersection.

Hint: Think of the X and Y dimensions independently.

NOTES:
- A better approach is to focus on conditions under which it can be guaranteed
that the rectangles to _not_ intersect.
- The time complexity is O(1), since the number of operations is constant.

"""

from collections import namedtuple

Rectangle = namedtuple('Rectangle', ('x', 'y', 'width', 'height'))


def intersect_rectangle(R1, R2):
    def is_intersect(R1, R2):
        return (
            R1.x <= R2.x + R2.width and R1.x + R1.width >= R2.x and \
            R1.y <= R2.y + R2.height and R1.y + R1.height >= R2.y
        )

    if not is_intersect(R1, R2):
        return Rectangle(0, 0, -1, -1)
    return Rectangle(
        max(R1.x, R2.x),
        max(R1.y, R2.y),
        min(R1.x + R1.width, R2.x + R2.width) - max(R1.x, R2.x),
        min(R1.y + R1.height, R2.y + R2.height) - max(R1.y, R2.y)
    )
