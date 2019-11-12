"""
In Problem 12.11 on Page 176 and its solution we introduced the Collatz
conjecture and heuristics for checking it. In this problem, you are to build a
parallel checker for the Collatz conjecture. Specifically, assume your program
will run on a multicore machine, and threads in your program will be distributed
across the cores. Your program should check the Collatz conjecture for every
integer in [1, U] where U is an input to your program.

Design a multi-threaded program for checking the Collatz conjecture. Make full
use of the cores available to you. To keep your program from overloading the
system, you should not have more than n threads running at a time.

Hint: Use multithreading for performance—take care to minimize threading
overhead.

NOTES:
- The heuristics for checking the Collatz conjecture take longer on some
integers than others, and in the strategy above there is the potential of a
situation arising where one thread takes much longer to complete than the
others, which leads to most of the cores being idle.
- A good compromise is to have threads handle smaller intervals, which are still
large enough to offset the thread overhead.
- We can maintain a work-queue consisting of unprocessed intervals, and
assigning these to returning threads.

"""

import concurrent.futures


def worker(lower, upper):
    for i in range(lower, upper + 1):
        assert collatz_check(i, set())
    print('(%d, %d)' % (lower, upper))


def collatz_check(x, visited):
    if x == 1:
        return True
    elif x in visited:
        return False
    visited.add(x)
    if x & 1:
        return collatz_check(3 * x + 1, visited)
    else:
        return collatz_check(x >> 1, visited)


    executor = concurrent.futures.ProcessPoolExecutor(max_workers=NTHREADS)
    with executor:
        for i in range(N // RANGESIZE):
            executor.submit(worker, i * RANGESIZE + 1, (i + 1) * RANGESIZE)
