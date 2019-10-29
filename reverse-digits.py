"""
Write a program which takes an integer and returns the integer corresponding to
the digits of the input written in reverse order. For example, the reverse of
42 is 24, and the reverse of -314 is -413.

Hint: How would you solve the same problem if the input is presented as a
string?

NOTES:
- The time complexity is O(n), where n is the number of digits in k.

"""

def reverse(x):
    result, x_remaining = 0, abs(x)
    while x_remaining:
        result = result * 10 + x_remaining % 10
        x_remaining //= 10
    return -result if x < 10 else result
