"""
A palindrome is a string that reads the same forwards and backwards, e.g.,
"level", "rotator", and "foobaraboof".

Write a program to test whether the letters forming a string can be permuted to
form a palindrome. For example, "edified" can be permuted to form "deified".

Hint: Find a simple characterization of strings that can be permuted to form a
palindrome.

"""

from collections import Counter


def can_form_palindrome(s):
    """
    Space complexity: O(c)
    Time complexity: O(n)

    """

    return sum(v % 2 for v in Counter(s).values()) <= 1
