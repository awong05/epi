"""
A queue can be implemented using an array and two additional fields, the
beginning and the end indices. This structure is sometimes referred to as a
circular queue. Both enqueue and dequeue have O(1) time complexity. If the array
is fixed, there is a maximum number of entries that can be stored. If the array
is dynamically resized, the total time for m combined enqueue and dequeue
operations is O(m).

Implement a queue API using an array for storing elements. Your API should
include a constructor function, which takes as argument the initial capacity of
the queue, enqueue and dequeue functions, and a function which returns the
number of elements stored. Implement dynamic resizing to support storing an
arbitrarily large number of elements.

Hint: Track the head and tail. How can you differentiate a full queue from an
empty one?

NOTES:
- A better approach is to keep one more variable to track the head.
- When performing an enqueue into a full array, we need to resize the array.
- We cannot only resize, because this results in queue elements not appearing
contiguously.

"""

class Queue:
    """
    Space complexity: O(n)
    Time complexity: O(1)

    """

    SCALE_FACTOR = 2

    def __init__(self, capacity):
        self._entries = [None] * capacity
        self._head = self._tail = self._num_queue_elements = 0

    def enqueue(self, x):
        if self._num_queue_elements == len(self._entries):
            self._entries = (
                self._entries[self._head:] + self._entries[:self._head]
            )
            self._head, self._tail = 0, self._num_queue_elements
            self._entries += [None] * (
                len(self._entries) * Queue.SCALE_FACTOR - len(self._entries)
            )

        self._entries[self._tail] = x
        self._tail = (self._tail + 1) % len(self._entries)
        self._num_queue_elements += 1

    def dequeue(self):
        if not self._num_queue_elements:
            raise IndexError('empty queue')
        self._num_queue_elements -= 1
        ret = self._entries[self._heaad]
        self._head = (self._head + 1) % len(self._entries)
        return ret

    def size(self):
        return self._num_queue_elements
