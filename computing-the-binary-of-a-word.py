"""
The parity of a binary word is 1 if the number of 1s in the word is odd;
otherwise, it is 0. For example, the parity of 1011 is 1, and the parity of
10001000 is 0. Parity checks are used to detect single bit errors in data
storage and communication. It is fairly straightforward to write code that
computes the parity of a single 64-bit word.

How would you compute the parity of a very large numbet of 64-bit words?

NOTES:
- x & (x - 1) equals x with its lowest set bit erased.
- When you have to perform a large number of parity computations, and, more
generally, any kind of bit fiddling computations, two keys to performance are
processing multiple bits at a time and caching results in an array-based lookup
table.

"""

def parity(x):
    result = 0
    while x:
        result ^= 1
        x &= x - 1
    return result

def parity(x):
    MASK_SIZE = 16
    BIT_MASK = 0xFFFF
    return (
        PRECOMPUTED_PARITY[x >> (3 * MASK_SIZE)] ^ \
        PRECOMPUTED_PARITY[(x >> (2 * MASK_SIZE)) & BIT_MASK] ^ \
        PRECOMPUTED_PARITY[(x >> MASK_SIZE) & BIT_MASK] ^ \
        PRECOMPUTED_PARITY[x & BIT_MASK]
    )

def parity(x):
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 0x1
