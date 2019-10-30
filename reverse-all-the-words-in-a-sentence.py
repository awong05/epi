"""
Given a string containing a set of words separated by whitespace, we would like
to transform it to a string in which the words appear in the reverse order. For
example, "Alice likes Bob" transforms to "Bob likes Alice". We do not need to
keep the original string.

Implement a function for reversing the words in a string s.

Hint: It's difficult to solve this with one pass.

"""

def reverse_words(s):
    """
    Space complexity: O(1)
    Time complexity: O(n)

    """

    s.reverse()

    def reverse_range(s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start, end = start + 1, end - 1

    start = 0
    while True:
        end = s.find(b' ', start)
        if end < 0:
            break
        reverse_range(s, start, end - 1)
        start = end + 1
    reverse_range(s, start, len(s) - 1)
