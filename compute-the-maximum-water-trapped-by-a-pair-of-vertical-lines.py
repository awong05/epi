"""
An array of integers naturally defines a set of lines parallel to the Y-axis,
starting from x = 0 as illustrated in Figure 17.4(a). The goal of this problem
is to find the pair of lines that together with the X-axis "trap" the most
water. See Figure 17.4(b) for an example.

Write a program which takes as input an integer array and returns the pair of
entries that trap the maximum amount of water.

Hint: Start with 0 and n - 1 and work your way in.

NOTES:
- Suppose A[0] > A[n - 1].
- Then for any k > 0, the water trapped between k and n - 1 is less than the
water trapped between 0 and n - 1, so going forward, we only need to focus on
the maximum water that can be trapped between 0 and n - 2.

"""

def get_max_trapped_water(heights):
    """
    Space complexity: O(1)
    Time complexity: O(n)

    """

    i, j, max_water = 0, len(heights) - 1, 0
    while i < j:
        width = j - i
        max_water = max(max_water, width * min(heights[i], heights[j]))
        if heights[i] > heights[j]:
            j -= 1
        else:
            i += 1
    return max_water
