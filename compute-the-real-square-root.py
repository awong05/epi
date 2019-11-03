"""
Square root computations can be implemented using sophisticated numerical
techniques involving iterative methods and logarithms. However, if you were
asked to implement a square root function, you would not be expected to know
these techniques.

Implement a function which takes as input a floating point value and returns its
square root.

Hint: Iteratively compute a sequence of intervals, each contained in the
previous interval, that contain the result.

NOTES:
- We cannot start with [0,x] because the square root may be larger than x, e.g.,
sqrt(1/4) = 1/2.
- However, if x >= 1.0, we can tighten the lower and upper bounds to 1.0 and x,
respectively, since if 1.0 <= x then x <= x**2.
- On the other hand, if x < 1.0, we can use x and 1.0 as the lower and upper
bounds respectively, since then the square root of x is greater than x but less
than 1.0.

"""

from math import isclose


def square_root(x):
    """
    Space complexity: O(1)
    Time complexity: O(log(x/s))

    """

    left, right = (x, 1.0) if x < 1.0 else (1.0, x)

    while not isclose(left, right):
        mid = 0.5 * (left + right)
        mid_squared = mid * mid
        if mid_squared > x:
            right = mid
        else:
            left = mid
    return left
