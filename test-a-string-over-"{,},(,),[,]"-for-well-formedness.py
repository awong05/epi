"""
A string over the characters "{,},(,),[,]" is said to be well-formed if the
different types of brackets match in the correct order.

For example, "([]){()}" is well-formed, as is "[()[]{()()}]". However, "{)",
"()", and "[()[]{()()" are not well-formed.

Write a program that tests if a string made up of the characters, '(',')','[',
']','{','}' is well-formed.

Hint: Which left parenthesis does a right parenthesis match with?

"""

def is_well_formed(s):
    """
    Space complexity: O(n)
    Time complexity: O(n)

    """

    left_chars, lookup = [], {'(': ')', '{': '}', '[': ']'}
    for c in s:
        if c in lookup:
            left_chars.append(c)
        elif not left_chars or lookup[left_chars.pop()] != c:
            return False
    return not left_chars
