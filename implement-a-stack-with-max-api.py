"""
Design a stack that includes a max operation, in addition to push and pop. The
max method should return the maximum value stored in the stack.

Hint: Use additional storage to track the maximum value.

"""

from collections import namedtuple


class Stack:
    """
    Space complexity: O(n)
    Time complexity: O(1)

    """

    ElementWithCachedMax = namedtuple(
        'ElementWithCachedMax',
        ('element', 'max')
    )

    def __init__(self):
        self._element_with_cached_max = []

    def empty(self):
        return len(self._element_with_cached_max) == 0

    def max(self):
        if self.empty():
            raise IndexError('max(): empty stack')
        return self._element_with_cached_max[-1].max

    def pop(self):
        if self.empty():
            raise IndexError('pop(): empty stack')
        return self._element_with_cached_max.pop().element

    def push(self, x):
        self._element_with_cached_max.append(
            self.ElementWithCachedMax(x, x if self.empty() else \
                max(
                    x, self.max()
                )
            )
        )

class Stack:
    """
    Space complexity: O(n)
    Time complexity: O(1)

    """

    class MaxWithCount:
        def __init__(self, max, count):
            self.max, self.count = max, count

    def __init__(self):
        self._element = []
        self._cached_max_with_count = []

    def empty(self):
        return len(self._element) == 0

    def max(self):
        if self.empty():
            raise IndexError('max(): empty stack')
        return self._cached_max_with_count[-1].max

    def pop(self):
        if self.empty():
            raise IndexError('pop(): empty stack')
        pop_element = self._element.pop()
        current_max = self._cached_max_with_count[-1].max
        if pop_element == current_max:
            self._cached_max_with_count[-1].count -= 1
            if self._cached_max_with_count[-1].count == 0:
                self._cached_max_with_count.pop()
        return pop_element

    def push(self, x):
        self._element.append(x)
        if len(self._cached_max_with_count) == 0:
            self._cached_max_with_count.append(self.MaxWithCount(x, 1))
        else:
            current_max = self._cached_max_with_count[-1].max
            if x == current_max:
                self._cached_max_with_count[-1].count += 1
            elif x > current_max:
                self._cached_max_with_count.append(self.MaxWithCount(x, 1))
