"""
A thief breaks into a clock store. Each clock has a weight and a value, which
are known to the thief. His knapsack cannot hold more than a specified combined
weight. His intention is to take clocks whose total value is maximum subject to
the knapsack's weight constant.

His problem is illustrated in Figure 16.8 on the next page. If the knapsack can
hold at most 130 ounces, he cannot take all the clocks. If he greedily chooses
clocks, in decreasing order of value-to-weight ratio, he will choose P,H,O,B,I,
and L in that order for a total value of $669. However, {H,J,O} is the optimum
selection, yielding a total value of $695.

Write a program for the knapsack problem that selects a subset of items that has
maximum value and satisfies the weight constraint. All items have integer
weights and values. Return the value of the subset.

Hint: Greedy approaches are doomed.

"""

from collections import namedtuple


Item = namedtuple('Item', ('weight', 'value'))


def optimum_subject_to_capacity(items, capacity):
    """
    Space complexity: O(nw)
    Time complexity: O(nw)

    """

    def optimum_subject_to_item_and_capacity(k, available_capacity):
        if k < 0:
            return 0

        if V[k][available_capacity] == -1:
            without_curr_item = optimum_subject_to_item_and_capacity(
                k - 1,
                available_capacity
            )
            with_curr_item = (0 if available_capacity < items[k].weight else \
                (items[k].value + optimum_subject_to_item_and_capacity(
                    k - 1,
                    available_capacity - items[k].weight
                ))
            )
            V[k][available_capacity] = max(without_curr_item, with_curr_item)
        return V[k][available_capacity]

    V = [[-1] * (capacity + 1) for _ in items]
    return optimum_subject_to_item_and_capacity(len(items) - 1, capacity)
