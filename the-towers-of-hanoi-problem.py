"""
A peg contains rings in sorted order, with the largest ring being the lowest.
You are to transfer these rings to another peg, which is initially empty. This
is illustrated in Figure 15.2.

Write a program which prints the sequence of operations that transfers n rings
from one peg to another. You have a third peg, which is initially empty. The
only operation you can perform is taking a single ring from the top of one peg
and placing it on the top of another peg. You must never place a larger ring
above a smaller ring.

Hint: If you know how to transfer the top n - 1 rings, how does that help move
the nth ring?

"""

NUM_PEGS = 3


def compute_tower_hanoi(num_rings):
    """
    Time complexity: O(2**n)

    """

    def compute_tower_hanoi_steps(num_rings_to_move, from_peg, to_peg, use_peg):
        if num_rings_to_move > 0:
            compute_tower_hanoi_steps(
                num_rings_to_move - 1,
                from_peg,
                use_peg,
                to_peg
            )
            pegs[to_peg].append(pegs[from_peg].pop())
            result.append([from_peg, to_peg])
            compute_tower_hanoi_steps(
                num_rings_to_move - 1,
                use_peg,
                to_peg,
                from_peg
            )

    result = []
    pegs = [list(reversed(range(1, num_rings_to_move + 1)))] + [[] for _ in range(1, NUM_PEGS)]
    compute_tower_hanoi_steps(num_rings, 0, 1, 2)
    return result
