"""
A sequence of integer arrays in which the nth array consists of n entries
corresponds to a triangle of numbers. See Figure 16.10 for an example.

Define a path in the triangle to be a sequence of entries in the triangle in
which adjacent entries in the sequence correspond to entries that are adjacent
in the triangle. The path must start at the top, descend the triangle
continuously, and end with an entry on the bottom row. The weight of a path is
the sum of the entries.

Write a program that takes as input a triangle of numbers and returns the weight
of a minimum weight path. For example, the minimum weight path for the number
triangle in Figure 16.10 is shown in bold face, and its weight is 15.

Hint: What property does the prefix of a minimum weight path have?

"""

def minimum_path_weight(triangle):
    """
    Space complexity: O(n)
    Time complexity: O(n**2)

    """

    min_weight_to_curr_row = [0]
    for row in triangle:
        min_weight_to_curr_row = [
            row[j] +
            min(min_weight_to_curr_row[max(j - 1, 0)],
                min_weight_to_curr_row[min(j, len(min_weight_to_curr_row) - 1)])
            for j in range(len(row))
        ]
    return min(min_weight_to_curr_row)
