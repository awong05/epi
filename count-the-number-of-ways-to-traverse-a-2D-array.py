"""
In this problem you are to count the number of ways of starting at the top-left
corner of a 2D array and getting to the bottom-right corner. All moves must
either go right or down. For example, we show three ways in a 5 x 5 2D array in
Figure 16.5. (As we will see, there are a total of 70 possible ways for this
example.)

Write a program that counts how many ways you can go from the top-left to the
bottom-right in a 2D array.

Hint: If i > 0 and j > 0, you can get to (i, j) from (i - 1, j) or (i, j - 1).

NOTES:
- There are (n+m-2 over n-1) = (n+m-2 over m-1) = (n+m-2)!/((n-1)!(m-1)!) such
paths.

"""

def number_of_ways(n, m):
    """
    Space complexity: O(nm)
    Time complexity: O(nm)

    """

    def compute_number_of_ways_to_xy(x, y):
        if x == y == 0:
            return 1

        if number_of_ways[x][y] == 0:
            ways_top = 0 if x == 0 else compute_number_of_ways_to_xy(x - 1, y)
            ways_left = 0 if y == 0 else compute_number_of_ways_to_xy(x, y - 1)
            number_of_ways[x][y] = ways_top + ways_left
        return number_of_ways[x][y]

    number_of_ways = [[0] * m for _ in range(n)]
    return compute_number_of_ways_to_xy(n - 1, m - 1)
