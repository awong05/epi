"""
If an array contains n - 1 integers, each between 0 and n - 1, inclusive, and
all numbers in the array are distinct, then it must be the case that exactly one
number between 0 and n - 1 is absent.

We can determine the missing number in O(n) time and O(1) space by computing the
sum of the elements in the array. Since the sum of all the numbers from 0 to
n - 1, inclusive, is (n-1)n/2, we can subtract the sum of the numbers in the
array from (n-1)n/2 to get the missing number.

For example, if the array is <5,3,0,1,2>, then n = 6. We subtract (5 + 3 + 0 + 1
+ 2) = 11 from 5(6)/2 = 15, and the result, 4, is the missing number.

Similarly, if the array contains n + 1 integers, each between 0 and n - 1,
inclusive, with exactly one element appearing twice, the duplicated integer will
be equal to the sum of the elements of the array minus (n-1)n/2.

Alternatively, for the first problem, we can compute the missing number by
computing the XOR of all the numbers from 0 to n - 1, inclusive, and XORing that
with the XOR of all the elements in the array. Every element in the array,
except for the missing element, cancels out with an integer from the first set.
Therefore, the resulting XOR equals the missing element. The same approach works
for the problem of finding the duplicated element. For example, the array
<5,3,0,1,2> represented in binary is <(101)2,(011)2,(000)2,(001)2,(010)2>. The
XOR of these entries is (101)2. The XOR of all numbers from 0 to 5, inclusive,
is (001)2. The XOR of (101)2 and (001)2 is (100)2 = 4, which is the missing
number.

We now turn to a related, though harder, problem.

You are given an array of n integers, each between 0 and n - 1, inclusive.
Exactly one element appears twice, implying that exactly one number between 0
and n - 1 is missing from the array. How would you compute the duplicate and
missing numbers?

Hint: Consider performing multiple passes through the array.

NOTES:
- Applying the same idea to the current problem, i.e., computing the XOR of all
the numbers from 0 to n - 1, inclusive, and the entries in the array, yields m
XOR t.
- However, since m != t, there must be some bit in m XOR t that is set to 1,
i.e., m and t differ in that bit.
- We compute the XOR of the numbers from 0 to n - 1 in which the kth bit is 1,
and the entries in the array in which the kth bit is 1.
- Let this XOR be h—by the logic described in the problem statement, h must be
one of m or t.

"""

from collections import namedtuple
from functools import reduce


DuplicateAndMissing = namedtuple(
    'DuplicateAndMissing',
    ('duplicate', 'missing')
)

def find_duplicate_missing(A):
    """
    Space complexity: O(1)
    Time complexity: O(n)

    """

    miss_XOR_dup = reduce(lambda v, i: v ^ i[0] ^ i[1], enumerate(A), 0)

    differ_bit, miss_or_dup = miss_XOR_dup & (~(miss_XOR_dup - 1)), 0
    for i, a in enumerate(A):
        if i & differ_bit:
            miss_or_dup ^= 1
        if a & differ_bit:
            miss_or_dup ^= a

    if miss_or_dup in A:
        return DuplicateAndMissing(miss_or_dup, miss_or_dup ^ miss_XOR_dup)
    return DuplicateAndMissing(miss_or_dup ^ miss_XOR_dup, miss_or_dup)
