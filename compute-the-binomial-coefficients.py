"""
The symbol (n over k) is the short form for the expression n(n-1)...(n-k+1)
over k(k-1)...(3)(2)(1). It is the number of ways to choose a k-element subset
from an n-element set. It is not obvious that the expression defining (n over k)
always yields an integer. Furthermore, direct computation of (n over k) from
this expression quickly results in the numerator or denominator overflowing if
integer types are used, even if the final result fits in a 32-bit integer. If
floats are used, the expression may not yield a 32-bit integer.

Design an efficient algorithm for computing (n over k) which has the property
that it never underflows if the final result fits in the integer word size.

Hint: Write an equation.

"""

def compute_binomial_coefficient(n, k):
    """
    Space complexity: O(nk)
    Time complexity: O(nk)

    """

    def compute_x_choose_y(x, y):
        if y in (0, x):
            return 1

        if x_choose_y[x][y] == 0:
            without_y = compute_x_choose_y(x - 1, y)
            with_y = compute_x_choose_y(x - 1, y - 1)
            x_choose_y[x][y] = without_y + with_y
        return x_choose_y[x][y]

    x_choose_y = [[0] * (k + 1) for _ in range(n + 1)]
    return compute_x_choose_y(n, k)
