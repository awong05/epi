"""
Consider a

How would you compute the k stars which are closest to Earth?

Hint: Suppose you know the k closest stars in the first n stars. If the
(n + 1)th star is to be added to the set of k closest stars, which element in
that set should be evicted?

"""

from heapq import heappop, heappush, nlargest
from math import sqrt


class Star:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    @property
    def distance(self):
        return sqrt(self.x**2 + self.y**2 + self.z**2)

    def __lt__(self, rhs):
        return self.distance < rhs.distance


def find_closest_k_stars(stars, k):
    """
    Space complexity: O(k)
    Time complexity: O(nlogk)

    """

    max_heap = []
    for star in stars:
        heappush(max_heap, (-star.distance, star))
        if len(max_heap) == k + 1:
            heappop(max_heap)

    return [s[1] for s in nlargest(k, max_heap)]
