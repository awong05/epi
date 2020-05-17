"""
In the pick-up-coins game, an even number of coins are placed in a line, as in
Figure 16.11. Two players take turns at choosing one coin each—they can only
choose from the two coins at the ends of the line. The game ends when all the
coins have been picked up. The player whose coins have the higher total value
wins. A player cannot pass his turn.

Design an efficient algorithm for computing the maximum total value for the
starting player in the pick-up-coins game.

Hint: Relate the best play for the first player to the best play for the second
player.

"""

def maximum_revenue(coins):
    """
    Time complexity: O(n**2)

    """

    def compute_maximum_revenue_for_range(a, b):
        if a > b:
            return 0

        if maximum_revenue_for_range[a][b] == 0:
            max_revenue_a = coins[a] + min(
                compute_maximum_revenue_for_range(a + 2, b),
                compute_maximum_revenue_for_range(a + 1, b - 1))
            max_revenue_b = coins[b] + min(
                compute_maximum_revenue_for_range(a + 1, b - 1),
                compute_maximum_revenue_for_range(a, b - 2))
            maximum_revenue_for_range[a][b] = max(max_revenue_a, max_revenue_b)
        return maximum_revenue_for_range[a][b]

    maximum_revenue_for_range = [[0] * len(coins) for _ in coins]
    return compute_maximum_revenue_for_range(0, len(coins) - 1)
