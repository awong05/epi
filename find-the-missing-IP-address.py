"""
The storage capacity of hard drives dwarfs that of RAM. This can lead to
interesting space-time trade-offs.

Suppose you were given a file containing roughly one billion IP addresses, each
of which is a 32-bit quantity. How would you programmatically find an IP address
that is not in the file? Assume

Hint: Can you be sure there is an address which is not in the file?

"""

from itertools import tee


def find_missing_element(stream):
    NUM_BUCKET = 1 << 16
    counter = [0] * NUM_BUCKET
    stream, stream_copy = tee(stream)
    for x in stream:
        upper_part_x = x >> 16
        counter[upper_part_x] += 1

    BUCKET_CAPACITY = 1 << 16
    candidate_bucket = next(
        i for i, c in enumerate(counter) if c < BUCKET_CAPACITY
    )

    candidates = [0] * BUCKET_CAPACITY
    stream = stream_copy
    for x in stream_copy:
        upper_part_x = x >> 16
        if candidate_bucket == upper_part_x:
            lower_part_x = ((1 << 16) - 1) & x
            candidates[lower_part_x] = 1

    for i, v in enumerate(candidates):
        if v == 0:
            return (candidate_bucket << 16) | i
