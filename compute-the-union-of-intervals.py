"""
In this problem we consider a set of intervals with integer endpoints; the
intervals may be open or closed at either end. We want to compute the union of
the intervals in such sets. A concrete example is given in Figure 13.2.

Design an algorithm that takes as input a set of intervals, and outputs their
union expressed as a set of disjoint intervals.

Hint: Do a case analysis.

"""

from collections import namedtuple


Endpoint = namedtuple('Endpoint', ('is_closed', 'val'))


class Interval:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __lt__(self, other):
        if self.left.val != other.left.val:
            return self.left.val < other.left.val
        return self.left.is_closed and not other.left.is_closed


def union_of_intervals(intervals):
    """
    Space complexity: O(1)
    Time complexity: O(nlogn)

    """

    if not intervals:
        return []

    intervals.sort()
    result = [intervals[0]]
    for i in intervals:
        if intervals and (i.left.val < result[-1].right.val or \
            (i.left.val == result[-1].right.val and \
                (i.left.is_closed or result[-1].right.is_closed))):
            if (i.right.val > result[-1].right.val or \
                (i.right.val  == result[-1].right.val and i.right.is_closed)):
                result[-1].right = i.right
        else:
            result.append(i)
    return result
