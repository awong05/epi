"""
Consider an object s which is read from and written to by many threads. (For
example, s could be the cache from Problem 19.1 on Page 291.) You need to ensure
that no thread may access s for reading or writing while another thread is
writing to s. (Two or more readers may access s at the same time.)

One way to achieve this is by protecting s with a mutex that ensures that two
threads cannot access s at the same time. However, this solution is suboptimal
because it is possible that a reader R1 has locked s and another reader R2 wants
to access s. Reader R2 does not have to wait until R1 is done reading; instead,
R2 should start reading right away.

This motivates the first readers-writers problem: protect s with the added
constraint that no reader is to be kept waiting if s is currently opened for
reading.

Implement a synchronization mechanism for the first readers-writers problem.

Hint: Track the number of readers.

NOTES:
- We want to keep track of whether the string is being read from, as well as
whether the string is being written to.
- Additionally, if the string is being read from, we want to know the number of
concurrent readers.
- We achieve this with a pair of locks—a read and write lock—and a read counter
locked by the read lock.

"""

from threading import Thread


class Reader(Thread):

    def run(self):
        while True:
            with RW.LR:
                RW.read_count += 1


            print(RW.data)
            with RW.LR:
                RW.read_count -= 1
                RW.LR.notify()
            do_something_else()


class Writer(Thread):

    def run(self):
        while True:
            with RW.LW:
                done = False
                while not done:
                    with RW.LR:
                        if RW.read_count == 0:
                            RW.data += 1
                            done = True
                        else:
                            while RW.read_count != 0:
                                RW.LR.wait()
            do_something_else()
