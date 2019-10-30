"""
In the decimal number system, the position of a digit is used to signify the
power of 10 that digit is to be multiplied with. For example, "314" denotes the
number 3 x 100 + 1 x 10 + 4 x 1. The base b number system generalizes the
decimal number system: The string "a(k-1)a(k-2)...a(1)a(0)", where 0<=a(i)<b,
denotes the base-b the integer a(0) x b**0 + a(1) x b**1 + a(2) x b**2 + ... +
a(k-1) x b**(k-1).

Write a program that performs base conversion. The input is a string, an integer
b(1), and another integer b(2). The string represents an integer in base b(1).
The output should be the string representing the integer in base b(2). Assume
2 <= b(1),b(2) <= 16. Use "A" to represent 10, "B" for 11, ..., and "F" for 15.
(For example, if the string is "615", b(1) is 7 and b(2) is 13, then the result
should be "1A7", since 6 x 7**2 + 1 x 7 + 5 = 1 x 13**2 + 10 x 13 + 7.)

Hint: What base can you easily convert to and from?

"""

from functools import reduce
from string import hexdigits


def convert_base(num_as_string, b1, b2):
    def construct_from_base(num_as_int, base):
        return (
            '' if num_as_int == 0 else \
            construct_from_base(num_as_int // base, base) + \
            hexdigits[num_as_int % base].upper()
        )

    is_negative = num_as_string[0] == '-'
    num_as_string = reduce(
        lambda x, c: x * b1 + hexdigits.index(c.lower()),
        num_as_string[is_negative:],
        0
    )
    return ('-' if is_negative else '') + \
        ('0' if num_as_int == 0 else construct_from_base(num_as_int, b2))
