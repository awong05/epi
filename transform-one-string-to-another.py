"""
Let s and t be strings and D a dictionary, i.e., a set of strings. Define s to
produce t if there exists a sequence of strings from the dictionary P = <s0,s1,
...,sn-1> such that the first string is s, the last string is t, and adjacent
strings have the same length and differ in exactly one character. The sequence P
is called a production sequence. For example, if the dictionary is {bat,cot,dog,
dag,dot,cat}, then <cat,cot,dot,dog> is production sequence.

Given a dictionary D and two strings s and t, write a program to determine if s
produces t. Assume that all characters are lowercase alphabets. If s does
produce t, output the length of the shortest production sequence; otherwise,
output -1.

Hint: Treat strings as vertices in an undirected graph, with an edge between u
and v if and only if the corresponding strings differ in one character.

"""

from collections import deque, namedtuple
from string import ascii_lowercase


def transform_string(D, s, t):
    """
    Time complexity: O(nd)

    """

    StringWithDistance = namedtuple(
        'StringWithDistance',
        ('candidate_string', 'distance')
    )
    q = deque([StringWithDistance(s, 0)])
    D.remove(s)

    while q:
        f = q.popleft()
        if f.candidate_string == t:
            return f.distance

        for i in range(len(f.candidate_string)):
            for c in ascii_lowercase:
                cand = f.candidate_string[:i] + c + f.candidate_string[i + 1:]
                if cand in D:
                    D.remove(cand)
                    q.append(StringWithDistance(cand, f.distance + 1))
    return -1
