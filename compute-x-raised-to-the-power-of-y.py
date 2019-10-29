"""
Write a program that takes a double x and an integer y and returns x**y. You can
ignore overflow and underflow.

Hint: Exploit mathematical properties of exponentiation.

NOTES:
- The number of multiplications is at most twice the index of y's MSB, implying
an O(n) time complexity.

"""

def power(x, y):
    result, power = 1.0, y
    if y < 0:
        power, x = -power, 1.0 / x
    while power:
        if power & 1:
            result *= x
        x, power = x * x, power >> 1
    return result
