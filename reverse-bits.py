"""
Write a program that takes a 64-bit unsigned integer and returns the 64-bit
unsigned integer consisting of the bits of the input in reverse order. For
example, if the input is (1110000000000001), the output should be
(1000000000000111).

Hint: Use a lookup table.

NOTES:
- The time complexity is identical to that for Solution 4.1 on Page 24, i.e.,
O(n/L), for n-bit integers and L-bit cache keys.

"""

def reverse_bits(x):
    MASK_SIZE = 16
    BIT_MASK = 0xFFFF
    return (
        PRECOMPUTED_REVERSE[x & BIT_MASK] << (3 * MASK_SIZE) | \
        PRECOMPUTED_REVERSE[(x >> MASK_SIZE) & BIT_MASK] << (2 * MASK_SIZE) | \
        PRECOMPUTED_REVERSE[(x >> (2 * MASK_SIZE)) & BIT_MASK] << MASK_SIZE | \
        PRECOMPUTED_REVERSE[(x >> (3 * MASK_SIZE)) & BIT_MASK]
    )
